from nicegui import ui, ui_run
import mysql.connector 
import os
from dotenv import load_dotenv
from serie import Serie

contenidos=[]
load_dotenv()




@ui.page("/")
def inicio():
    conexion = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user=os.getenv("USER"),
            password='',
            database=os.getenv("DB")
        )

    with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM contenidos")
            resultados_db = cursor.fetchall()
            # Procesar los resultados sin modificar la lista original durante la iteración
            for contenido in resultados_db:
                contenido=Serie(
                nombre=contenido[4],
                descripcion=contenido[2],
                categoria=contenido[3],
                episodios=contenido[0],
                temporadas=contenido[5]
                )
                ui.label(contenido.getnombre())
ui.run()