# MODELOS PARA LA PRACTICA 1 -------------------------------------------------------------------------------------------------------------

class Cadena():

    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.esOrdenado = False
        self.ordenado = []
        self.esBuscado = False
        self.buscado = {}
        self.numeros = []

# SETTERS

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEsOrdenado(self, esOrdenado):
        self.esOrdenado = esOrdenado

    def setOrdenado(self, ordenado):
        self.ordenado = ordenado

    def setEsBuscado(self, esBuscado):
        self.esBuscado = esBuscado

    def setBuscado(self, buscado):
        self.buscado = buscado

    def setNumeros(self, numeros):
        self.numeros = numeros

    def setNumero(self, numero):
        self.numeros.append(numero)

# GETTERS

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getEsOrdenado(self):
        return self.esOrdenado

    def getOrdenado(self):
        return self.ordenado

    def getEsBuscado(self):
        return self.esBuscado

    def getBuscado(self):
        return self.buscado
    
    def getNumeros(self):
        return self.numeros
