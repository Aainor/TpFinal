from multimedia import Multimedia
class Pelicula(Multimedia):
    def __init__(self, nombre, descripcion, categoria, duracion, rating):
        super().__init__(nombre, descripcion, categoria)
        self._duracion = duracion
        self._rating = rating

    def reproducir(self):
        h = super().reproducir()
        return f"{h} - Duración: {self._duracion} min - Rating: {self._rating}/10"
