# -*- coding: utf-8 -*-

import os

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
            break
        elif opcionMenu == "2":
            break
        elif opcionMenu == "3":
            break
        elif opcionMenu == "4":
            break
        else:
            print("")
