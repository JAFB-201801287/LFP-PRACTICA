# MODELOS PARA LA PRACTICA 1 -------------------------------------------------------------------------------------------------------------

class Cadena():

    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.ordenar = False
        self.buscar = False
        self.numeros = []

# SETTERS

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setOrdenar(self, ordenar):
        self.ordenar = ordenar

    def setBuscar(self, buscar):
        self.buscar = buscar

    def setNumeros(self, numeros):
        self.numeros = numeros

    def setNumero(self, numero):
        self.numeros.append(numero)

# GETTERS

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getOrdenar(self):
        return self.ordenar

    def getBuscar(self):
        return self.buscar
    
    def getNumeros(self):
        return self.numeros