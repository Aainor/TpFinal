from nicegui import ui, ui_run
import mysql.connector 
import os
from dotenv import load_dotenv
load_dotenv()
@ui.page("/")
def inicio():
    ui.label("bienvenido")


@ui.page("/contenidos")
def contenido():
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user=os.getenv("USER"),
        password='',
        database=os.getenv("DB")
    )
    ui.label("contenidos:")
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM contenido")
        contenidos = cursor.fetchall()
        for contenido in contenidos:
            ui.label(contenido)
    ui.run()
