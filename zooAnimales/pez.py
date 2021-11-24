from zooAnimales.animal import *

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    peces = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.peces.insert(self)

    @classmethod
    def cantidadPeces(cls):
        cls.peces.count()

    def getCantidadAletas(self):
        return self._cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, 'oceano', genero, 'rojo', 6)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, 'oceano', genero, 'gris', 6)
