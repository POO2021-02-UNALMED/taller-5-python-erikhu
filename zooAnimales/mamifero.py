from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    mamiferos = []
    def __init__(self, nombre='', edad=0, habitat='', genero='', pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.mamiferos.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.mamiferos)

    def getPatas(self):
        return self._patas

    def isPelaje(self):
        return self._pelaje

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, 'pradera', genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, 'selva', genero, True, 4)
