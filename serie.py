from multimedia import Multimedia

class Serie(Multimedia):
    def __init__(self, nombre, descripcion, categoria, episodios, temporadas):
        super().__init__(nombre, descripcion, categoria)
        self._episodios = episodios
        self._temporadas = temporadas
        
    def reproducir(self):
        h = super().reproducir()
        f"{h} {self.nombre}"

