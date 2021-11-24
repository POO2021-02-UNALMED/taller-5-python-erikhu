class Zoologico:
    def __init__(self, nombre='', ubicacion=''):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def getNombre(self):
        return self._nombre

    def getUbicacion(self):
        return self._ubicacion

    def agregarZonas(self, zona):
        self._zonas.insert(zona)

    def cantitadTotalAnimales(self):
        contador = 0
        for zona in  self._zonas:
            contador = contador + zona.cantidadAnimales()
        return contador
