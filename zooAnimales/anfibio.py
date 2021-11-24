from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    anfibios = []
    def __init__(self, nombre='', edad=0, habitat='', genero='', colorPiel='', venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.anfibios.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        cls.anfibios.count()

    def getVenenoso(self):
        return self._venenoso

    def getColorPiel(self):
        return self._colorPiel

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, 'selva', genero, 'negro y amarillo', False)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, 'selva', genero, 'rojo', True)
