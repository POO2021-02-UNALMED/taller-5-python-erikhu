

class Animal:
    totalAnimales = 0;

    def __init__(self, nombre='', edad=0, habitat='', genero=''):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def movimiento(self):
        return "desplazar"

    @classmethod
    def totalPorTipo(cls):
        import zooAnimales.anfibio
        import zooAnimales.mamifero
        import zooAnimales.ave
        import zooAnimales.reptil
        import zooAnimales.pez
        return "Mamiferos: {}\nAves: {}\nReptiles: {}\nPeces: {}\nAnfibios: {}".format(
            zooAnimales.mamifero.Mamifero.cantidadMamiferos(),
            zooAnimales.ave.Ave.cantidadAves(),
            zooAnimales.reptil.Reptil.cantidadReptiles(),
            zooAnimales.pez.Pez.cantidadPeces(),
            zooAnimales.anfibio.Anfibio.cantidadAnfibios())

    def toString(self):
        return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self._nombre, self._edad, self._habitat, self._genero)
