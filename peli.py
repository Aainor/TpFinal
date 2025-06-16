from multimedia import Multimedia
class Pelicula(Multimedia):
    def __init__(self, nombre, descripcion, categoria, duracion, rating):
        self._duracion = duracion
        self._rating = rating
        super().__init__(nombre, descripcion, categoria)

    def reproduccion(self):
        h = super().reproducir()
        f"{h} {self.nombre}"
