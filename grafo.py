import networkx as nx 
import json
from nicegui import ui
from usuario import Usuario
with open ("contents.json", "r", encoding= "utf-8") as file:
    datos = json.load(file)


class Lista:
    def __init__(self):
        self.grafo_series = nx.DiGraph()

    def cargar_json(self,datos):
        for serie in datos ["series"]:
            nombre = serie ["nombre"]
            self.grafo_series.add_node(nombre,
                                descripcion = serie["descripcion"],
                                tipo = serie["tipo"],
                                duracion = serie["duracion"],
                                categoria = serie["categoria"],
                                popularidad = serie["popularidad"])
            
        for nombre_serie, lista_episodios in datos["episodios"].items():
            anterior = None
            for ep in lista_episodios:
                id_ep = f"{nombre_serie}_ep{ep['episodio']}"
                self.grafo_series.add_node(id_ep, titulo = ep["titulo"], url = ep["url"])
                self.grafo_series.add_edge(nombre_serie,id_ep)
                if anterior:
                    self.grafo_series.add_edge(anterior, id_ep)
                anterior = id_ep

for nodo in Usuario.lista.grafo_series.nodes(data=True):
    ui.label(f"{nodo[0]}: {nodo[1].get('descripcion', 'Sin descripción')}")