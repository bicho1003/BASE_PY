import pandas as pd
import csv
import numpy as np

"""Escribir la BD"""
#Agregar
nombre  = input("Escribe el nombre: ")
archivo = open("BD.txt","a")
archivo.write(nombre+"\t")
archivo.close()

apellido  = input("Escribe el Apellido: ")
archivo = open("BD.txt","a")
archivo.write(apellido+"\t")
archivo.write("\n")
archivo.close()

#Txt a Array#
print("\tSe muestra la base de datos:\n")
a = np.loadtxt('BD.txt',dtype=str)
print(a)

#print("\tSe borra la Base de datos\n")


