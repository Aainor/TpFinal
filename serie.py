from multimedia import Multimedia

class Serie(Multimedia):
    def __init__(self, nombre, descripcion, categoria, episodios, temporadas):
        super().__init__(nombre, descripcion, categoria)
        self._episodios = episodios
        self._temporadas = temporadas
    def getnombre(self):
        return self._nombre
    def reproducir(self):
        h = super().reproducir()
        f"{h} {self.nombre}" #Y ESTE METODO DE VIRGO MOMO?
series=[]
def instanciarS(y):
    for x in y:
        content= Serie(
            nombre=x["nombre"],
            descripcion=x["descripcion"],
            categoria=x["categoria"],
            episodios=x["episodios"],
            temporadas=x["temporadas"]
        )
        series.append(content)
    return series