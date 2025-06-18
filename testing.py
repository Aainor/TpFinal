from nicegui import ui
import grafo
from usuario import Usuario
import json

with open(r"util/contents.json", "r", encoding="utf-8") as file:
    datos = json.load(file)


#creamos el usuario e incializamos la lista con el json
usuario = Usuario(1, "Franco", "lemhomo@gmail.com", "1234", historial=[])
usuario._lista.cargar_json(datos)

#accedemos al grafo
grafo = usuario._lista.grafo_series

#titulo
ui.label(f"Bienvenido, {usuario.nombre}").classes('text-2x1 font-bold')

#lista de series
ui.label("Series disponibles: ").classes("text-x1 mt-4")

for nodo, atributos in grafo.nodes(data=True):
    if "descripcion" in atributos: #es una serie, no un ep
        with ui.card().tight():
            ui.label(nodo).classes('text-lg font-semibold')
            ui.label(atributos["descripcion"])
            ui.button("Ver episodios", on_click=lambda s=nodo: mostrar_episodios(s)).props("flat color=primary")


def mostrar_episodios(serie_nombre):
    ui.dialog().open()
    with ui.dialog() as dialog:
        dialog.open()
        ui.label(f"Episodios de {serie_nombre}").classes("text-x1 font-bold")
        for vecino in grafo.successors(serie_nombre):
            ep = grafo.nodes[vecino]
            if "url" in ep:
                ui.label(f"{ep['titulo']}")
                ui.html(ep["url"])

