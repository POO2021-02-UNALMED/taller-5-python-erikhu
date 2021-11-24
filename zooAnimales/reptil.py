class Reptil(Animal):
    serpientes = 0
    iguanas = 0
    reptiles = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.reptiles.insert(self)

    @classmethod
    def cantidadReptiles(cls):
        cls.reptiles.count()

    def getLargoCola(self):
        return self._largoCola

    def getColorEscamas(self):
        return self._colorEscamas

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, 'humedal', genero, 'verde', 3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, 'jungla', genero, 'blanco', 1)