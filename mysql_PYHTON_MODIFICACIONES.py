import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox


class App:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Filtros con MySQL - Tema Oscuro")
        self.raiz.geometry("900x500")
        self.raiz.resizable(False, False)

        # ---------- TEMA OSCURO ----------
        self.raiz.configure(bg="#1e1e1e")  # Fondo oscuro

        style = ttk.Style()
        style.theme_use("default")

        # Combobox y botones oscuros
        style.configure("TLabel", background="#1e1e1e", foreground="white")
        style.configure("TButton", background="#333333", foreground="white", padding=6)
        style.map("TButton", background=[("active", "#555555")])
        style.configure("TCombobox", fieldbackground="#333333", background="#333333", foreground="white")

        # Tabla oscura
        style.configure("Treeview", background="#2d2d2d", foreground="white",
                        fieldbackground="#2d2d2d", rowheight=25)
        style.map("Treeview", background=[("selected", "#555555")])

        # ---------- VARIABLES ----------
        self.genero = tk.StringVar()
        self.estado = tk.StringVar()

        # ---------- ETIQUETAS ----------
        ttk.Label(raiz, text="Género").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(raiz, text="Estado civil").grid(row=0, column=1, padx=10, pady=5)

        # ---------- COMBOBOX ----------
        ttk.Combobox(
            raiz,
            values=("F", "M"),
            textvariable=self.genero,
            width=12,
            state="readonly"
        ).grid(row=1, column=0, padx=10)

        ttk.Combobox(
            raiz,
            values=("Married", "Single", "Divorced", "Widow"),
            textvariable=self.estado,
            width=18,
            state="readonly"
        ).grid(row=1, column=1, padx=10)

        # ---------- BOTONES ----------
        ttk.Button(
            raiz,
            text="Buscar",
            command=self.buscar_datos,
            width=18
        ).grid(row=2, column=0, pady=15)

        ttk.Button(
            raiz,
            text="Borrar",
            command=self.limpiar,
            width=18
        ).grid(row=2, column=1, pady=15)

        ttk.Button(
            raiz,
            text="Salir",
            command=self.raiz.destroy,
            width=18
        ).grid(row=2, column=2, pady=15, padx=10)

        # ---------- TABLA ----------
        self.tabla = ttk.Treeview(
            raiz,
            columns=("nombre", "genero", "estado", "telefono", "correo"),
            show="headings",
            height=12
        )

        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("genero", text="Género")
        self.tabla.heading("estado", text="Estado Civil")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("correo", text="Correo")

        self.tabla.column("nombre", width=180, anchor="center")
        self.tabla.column("genero", width=90, anchor="center")
        self.tabla.column("estado", width=140, anchor="center")
        self.tabla.column("telefono", width=140, anchor="center")
        self.tabla.column("correo", width=260, anchor="center")

        self.tabla.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

    # ---------- FUNCIÓN BUSCAR ----------
    def buscar_datos(self):

        genero = self.genero.get()
        estado = self.estado.get()

        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",  # Cambia tu contraseña
                database="DB_MYSQL"
            )

            cursor = conexion.cursor()

            query = """
            SELECT Nombre, Genero, Estado_Civil, Telefono, Correo
            FROM base_personal
            WHERE 1=1
            """
            valores = []

            if genero:
                query += " AND Genero = %s"
                valores.append(genero)

            if estado:
                query += " AND Estado_Civil = %s"
                valores.append(estado)

            cursor.execute(query, valores)
            resultados = cursor.fetchall()

            self.tabla.delete(*self.tabla.get_children())

            if resultados:
                for fila in resultados:
                    self.tabla.insert("", "end", values=fila)
            else:
                messagebox.showinfo("Sin resultados", "No se encontraron registros")

            conexion.close()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar o consultar\n\n{e}")

    # ---------- FUNCIÓN LIMPIAR ----------
    def limpiar(self):
        self.genero.set("")
        self.estado.set("")
        self.tabla.delete(*self.tabla.get_children())


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    raiz = tk.Tk()
    app = App(raiz)
    raiz.mainloop()
