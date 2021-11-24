class Ave(Animal):
    halcones = 0
    aguilas = 0
    aves = []
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.aves.insert(self)

    @classmethod
    def cantidadAves(cls):
        cls.aves.count()

    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, 'montanas', genero, 'cafe glorioso')

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, 'montanas', genero, True, 'blanco y amarillo')