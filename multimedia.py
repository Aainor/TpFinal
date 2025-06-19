class Multimedia:
    def __init__(self, nombre, descripcion, categoria):
        self._nombre = nombre
        self._descripcion = descripcion
        self._categoria = categoria

    def reproducir(self):
        return f"Reproduciendo {self._nombre}"
        