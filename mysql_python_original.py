import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox


class App:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Filtros con MySQL")
        self.raiz.geometry("820x450")
        self.raiz.resizable(False, False)

        # ---------- VARIABLES ----------
        self.genero = tk.StringVar()
        self.estado = tk.StringVar()

        # ---------- ETIQUETAS ----------
        tk.Label(raiz, text="Género").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(raiz, text="Estado civil").grid(row=0, column=1, padx=10, pady=5)

        # ---------- COMBOBOX ----------
        ttk.Combobox(
            raiz,
            values=("F", "M"),
            textvariable=self.genero,
            width=10,
            state="readonly"
        ).grid(row=1, column=0, padx=10)

        ttk.Combobox(
            raiz,
            values=("Married", "Single", "Divorced", "Widow"),
            textvariable=self.estado,
            width=15,
            state="readonly"
        ).grid(row=1, column=1, padx=10)

        # ---------- BOTONES ----------
        tk.Button(
            raiz,
            text="Buscar",
            command=self.buscar_datos,
            width=15
        ).grid(row=2, column=0, pady=15)

        tk.Button(
            raiz,
            text="Borrar",
            command=self.limpiar,
            width=15
        ).grid(row=2, column=1, pady=15)

        # ---------- TABLA ----------
        self.tabla = ttk.Treeview(
            raiz,
            columns=("nombre", "genero", "estado", "correo"),
            show="headings",
            height=12
        )

        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("genero", text="Género")
        self.tabla.heading("estado", text="Estado civil")
        self.tabla.heading("correo", text="Correo")

        self.tabla.column("nombre", width=200, anchor="center")
        self.tabla.column("genero", width=100, anchor="center")
        self.tabla.column("estado", width=140, anchor="center")
        self.tabla.column("correo", width=250, anchor="center")

        self.tabla.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    # ---------- FUNCIÓN BUSCAR ----------
    def buscar_datos(self):

        genero = self.genero.get()
        estado = self.estado.get()

        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",  # CAMBIA TU CONTRASEÑA
                database="DB_MYSQL"
            )

            cursor = conexion.cursor()

            query = """
            SELECT Nombre, Genero, Estado_Civil, Correo
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
            messagebox.showerror(
                "Error",
                f"No se pudo conectar o consultar\n\n{e}"
            )

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
