class Zona:
    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def getZoo(self):
        return self._zoo

    def getNombre(self):
        return self._nombre

    def agregarAnimales(self, animal):
        self._animales.insert(animal)

    def cantidadAnimales(self):
        return self._animales.count()
