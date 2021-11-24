from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    mamiferos = []
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.mamiferos.insert(self)

    @classmethod
    def cantidadMamiferos(cls):
        cls.mamiferos.count()

    def getPatas(self):
        return self._patas

    def getPelaje(self):
        return self._pelaje

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, 'pradera', genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, 'selva', genero, True, 4)
