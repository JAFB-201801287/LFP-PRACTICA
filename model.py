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
        self.texto = ''

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

    def setTexto(self, texto):
        self.texto = texto

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

    def getTexto(self):
        return self.texto

class CadenaController():
    __instance = None
    index = 0
    cadenas = []

    def get(self):
        return self.cadenas

    def getPuestos(self):
        return self.puestos

# Constructor ----------------------------------------

    def __str__(self):
        return self.cadenas

    def __new__(cls):
        if CadenaController.__instance is None:
            CadenaController.__instance = object.__new__(cls)
        return CadenaController.__instance

    def __init__(self):
        self.id = 0

# Metodos ---------------------------------------------

    def get(self):
        return self.cadenas

    def add(self, cadena):
        self.cadenas.append(cadena)

    def clean(self):
        self.cadenas = []