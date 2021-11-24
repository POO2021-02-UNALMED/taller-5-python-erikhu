from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    peces = []
    def __init__(self, nombre='', edad=0, habitat='', genero='', colorEscamas='', cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.peces.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls.peces)

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
