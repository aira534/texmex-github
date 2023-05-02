#!/usr/bin/python3
import sys

#Abrir archivo con su ruta relativa a este fichero
with open ('recetas.md','r') as archivo:
    #Leerlo
    contenido=archivo.read()
    #Imprimirlo
    print(contenido)

sys.exit(0)
