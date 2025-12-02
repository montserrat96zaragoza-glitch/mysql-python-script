# Proyecto: Filtros MySQL con Python y Tkinter

Este proyecto es una interfaz gráfica construida en **Python**, utilizando:

- Tkinter (GUI)
- MySQL Connector (conexión a base de datos)
- Treeview (visualización de datos en tabla)

## Funcionalidad principal

La aplicación permite:

- Buscar registros por:
  - Género
  - Estado civil
  - Teléfono (nueva columna agregada)
- Mostrar resultados en tabla
- Limpiar filtros
- Salir de la aplicación
- Tema oscuro (Dark Mode)

## Base de datos

La aplicación se conecta a la base **DB_MYSQL**, consultando la tabla (creadando la conexión de excel con python y cargada a sql):

base_personal

diff
Copiar código

Campos obligatorios:

- Nombre  
- Genero  
- Estado_Civil  
- Correo  
- Telefono  

## Ejecución

python tarea_mysql.py

shell
Copiar código

## Requisitos

Instala dependencias:


pip install mysql-connector-python

shell
Copiar código

## Tema Oscuro


La interfaz fue personalizada utilizando estilos ttk para lograr un modo oscuro total.

## 👤 Autor

Montserrat — Maestría en Ciencia de Datos
