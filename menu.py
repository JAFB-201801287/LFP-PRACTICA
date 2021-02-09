# -*- coding: utf-8 -*-

import os
import re
import webbrowser

import lectorArchivos as LectorArchivo
from model import Cadena, CadenaController

def clean():  # Metodo para limpiar pantalla
    os.system("cls")

def caratula():
    print("==".title().center(150, "="))
    print("\tLENGUAJES FORMALES")
    print("\tSECCION A-")
    print("\t201801287")
    print("==".title().center(150, "="))

def menu():
    clean()
    while True:
        caratula()
        print("\tMENU PRACTICA 1")
        print("==".title().center(150, "="))
        print("\t1) - CARGAR ARCHIVOS DE ENTRADA:")
        print("\t2) - DESPLEGAR LISTAS ORDENADAS:")
        print("\t3) - DESPLEGAR BUSQUEDAS:")
        print("\t4) - DESPLEGAR TODAS:")
        print("\t5) - DESPLEGAR TODAS A ARCHIVO HTML:")
        print("\t6) - Salir:")
        print("--".title().center(150, "-"))
        print("")

        # solicituamos una opción al usuario
        print("ESCRIBA EL NUMERO DE LA OPCION QUE DECEA REALIZAR.")
        opcionMenu = input("Insertar Valor De La Opción >> ")
        print("--".title().center(150, "-"))

        if opcionMenu == "1":
            cargarArchivo()
        elif opcionMenu == "2":
            verListasOrdenadas()
        elif opcionMenu == "3":
            verBusqueda()
        elif opcionMenu == "4":
            verTodo()
        elif opcionMenu == "5":
            crearhtml()
        elif opcionMenu == "6":
            clean()
            break
        else:
            print("")
        clean()

def cargarArchivo():
    id = 0
    lineas = LectorArchivo.leerArchivo()
    for linea in lineas:
        id += 1
        cadena = Cadena()
        expresion_regular = ''
        identificador = ''
        lista = []
        lista_ordenada = []
        esOrdenada = False
        buscar = ''
        esBuscado = False
        if(re.search('BUSCAR', linea) != None and re.search('ORDENAR', linea) != None):
            if(re.search('ORDENAR', linea).span()[0] < re.search('BUSCAR', linea).span()[0]):
                expresion_regular = r"(?P<identificador>\w+)\s*=\s*(?P<lista>[\d+,\s*_]+\s*[0-9]+)\s*(?P<ordenar>ORDENAR)\s*,\s*BUSCAR\s*(?P<buscar>[0-9]+)\s*"
            elif(re.search('BUSCAR', linea).span()[0] < re.search('ORDENAR', linea).span()[0]):
                expresion_regular = r"(?P<identificador>\w+)\s*=\s*(?P<lista>[\d+,\s*_]+\s*[0-9]+)\s*BUSCAR\s*(?P<buscar>[0-9]+),\s*(?P<ordenar>ORDENAR)\s*"

            a = re.match(expresion_regular, linea)
            identificador = a.group('identificador')
            lista = a.group('lista').replace(' ', '').split(',')
            lista_ordenada = ordenarLista(a.group('lista').replace(' ', '').split(','))
            esOrdenada = True
            buscar = a.group('buscar')
            esBuscado = True

        elif(re.search('BUSCAR', linea) != None and re.search('ORDENAR', linea) == None):
            expresion_regular = r"(?P<identificador>\w+)\s*=\s*(?P<lista>[\d+,\s*_]+\s*[0-9]+)\s*BUSCAR\s*(?P<buscar>[0-9]+)\s*"

            a = re.match(expresion_regular, linea)
            identificador = a.group('identificador')
            lista = a.group('lista').replace(' ', '').split(',')
            lista_ordenada = ordenarLista(a.group('lista').replace(' ', '').split(','))
            esOrdenada = False
            buscar = a.group('buscar')
            esBuscado = True

        elif(re.search('BUSCAR', linea) == None and re.search('ORDENAR', linea) != None):
            expresion_regular = r"(?P<identificador>\w+)\s*=\s*(?P<lista>[\d+,\s*_]+\s*[0-9]+)\s*(?P<ordenar>ORDENAR)\s*"

            a = re.match(expresion_regular, linea)
            identificador = a.group('identificador')
            lista = a.group('lista').replace(' ', '').split(',')
            lista_ordenada = ordenarLista(a.group('lista').replace(' ', '').split(','))
            esOrdenada = True
            buscar = ''
            esBuscado = False
        cadena.setId(id)
        cadena.setTexto(linea)
        cadena.setNombre(identificador)
        cadena.setEsOrdenado(esOrdenada)
        cadena.setOrdenado(lista_ordenada)
        cadena.setEsBuscado(esBuscado)
        cadena.setBuscado(buscar)
        cadena.setNumeros(lista)
        CadenaController().add(cadena)
    input('SE A INGRESADO LA INFORMACION DEL ARCHIVO.\nPRESIONE CUALQUIER TECLA PARA REGRESAR AL MENU.')

def verListasOrdenadas():
    print("__".title().center(150, "_"))
    print('DESPLEGAR LISTAS ORDENADAS')
    print("--".title().center(150, "-"))
    for cadena in CadenaController().get():
        if(cadena.getEsOrdenado()):
            lista_ordenada = str(cadena.getOrdenado()).replace('[', '').replace(']', '')
            print(f'{cadena.getNombre()}: LISTA ORDENADA = {lista_ordenada}')
    print("--".title().center(150, "-"))
    print('')
    input('PRESIONE CUALQUIER TECLA PARA REGRESAR AL MENU.')

def verBusqueda():
    print("__".title().center(150, "_"))
    print('DESPLEGAR BUSQUEDAS')
    print("--".title().center(150, "-"))
    for cadena in CadenaController().get():
        if(cadena.getEsBuscado()):
            contador = 0
            encontrado = ''
            lista = cadena.getNumeros()
            for l in lista:
                contador += 1
                if(contador == len(lista) and cadena.getBuscado() == l):
                    encontrado += str(contador)
                elif(cadena.getBuscado() == l):
                    encontrado += f'{str(contador)}, '
            print('')
            print(f'LINEA {cadena.getId()}')
            if(encontrado != ''):
                print(f'{cadena.getNombre()}: POSICIONES DEL {cadena.getBuscado()} = {encontrado}')
            else:
                print(f'{cadena.getNombre()}: POSICIONES DEL {cadena.getBuscado()} = NO ENCONTRADO')
    print("--".title().center(150, "-"))
    print('')
    input('PRESIONE CUALQUIER TECLA PARA REGRESAR AL MENU.')

def verTodo():
    print("__".title().center(150, "_"))
    print('DESPLEGAR TODAS')
    print("--".title().center(150, "-"))
    for cadena in CadenaController().get():
        print('')
        print(f'LINEA {cadena.getId()}')
        print(cadena.getTexto())
        if(cadena.getEsOrdenado()):
                lista_ordenada = str(cadena.getOrdenado()).replace('[', '').replace(']', '')
                print(f'{cadena.getNombre()}: LISTA ORDENADA = {lista_ordenada}')
        if(cadena.getEsBuscado()):
            contador = 0
            encontrado = ''
            lista = cadena.getNumeros()
            for l in lista:
                contador += 1
                if(contador == len(lista) and cadena.getBuscado() == l):
                    encontrado += str(contador)
                elif(cadena.getBuscado() == l):
                    encontrado += f'{str(contador)}, '
            if(encontrado != ''):
                print(f'{cadena.getNombre()}: POSICIONES DEL {cadena.getBuscado()} = {encontrado}')
            else:
                print(f'{cadena.getNombre()}: POSICIONES DEL {cadena.getBuscado()} = NO ENCONTRADO')
    print("--".title().center(150, "-"))
    print('')
    input('PRESIONE CUALQUIER TECLA PARA REGRESAR AL MENU.')

def crearhtml():
    title = '\n\t\t<title>PRACTICA 1</title>'
    meta = '\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    estilo = '\n\t\t<link rel="stylesheet" href="style.css" />'
    cabeza = f'\n\t<head>{title}{meta}{estilo}\n\t</head>\n'
    contenido = ''
    for cadena in CadenaController().get():
        elemento1 = f'\n\t\t\t\t<p>IDENTIFICADOR: {cadena.getNombre()}</p>'
        elemento2 = f'\n\t\t\t\t<p>LINEA: {cadena.getId()}</p>'
        elemento3 = f'\n\t\t\t\t<p>{cadena.getTexto()}</p>'
        elemento4 = ''
        elemento5 = ''
        if(cadena.getEsOrdenado()):
            lista_ordenada = str(cadena.getOrdenado()).replace('[', '').replace(']', '')
            elemento4 = f'\n\t\t\t\t<p>LISTA ORDENADA: {lista_ordenada}</p>'
        if(cadena.getEsBuscado()):
            contador = 0
            encontrado = ''
            lista = cadena.getNumeros()
            for l in lista:
                contador += 1
                if(contador == len(lista) and cadena.getBuscado() == l):
                    encontrado += str(contador)
                elif(cadena.getBuscado() == l):
                    encontrado += f'{str(contador)}, '
            if(encontrado != ''):
                elemento5 = f'\n\t\t\t\t<p>POSICIONES DEL {cadena.getBuscado()}: {encontrado}</p>'
            else:
                elemento5 = f'\n\t\t\t\t<p>POSICIONES DEL {cadena.getBuscado()}: NO ENCONTRADO</p>'

        contenido += f'\n\t\t\t<div>{elemento1}{elemento2}{elemento3}{elemento4}{elemento5}\n\t\t\t</div>\n\t\t\t\t<br>'


    cuerpo = f'\n\t<body>\n\t\t<h1>DESPLEGAR TODAS A ARCHIVO HTML</h1>\n\t\t<div class="grid-container">{contenido}\n\t\t</div>\n\t</body>'
    html = f'<!DOCTYPE html>\n<html lang="es">{cabeza}{cuerpo}\n</html>'

    archivo = open("PAGINA.html", 'w')
    archivo.write(html)
    archivo.close()

    new = 2 # open in a new tab, if possible
    filename = 'file://' + os.path.realpath('PAGINA.html')
    webbrowser.open(filename, new=new)

    print('')
    input('PRESIONE CUALQUIER TECLA PARA REGRESAR AL MENU.')
    

def ordenarLista(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista