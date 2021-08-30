import pandas as pd
import csv
import numpy as np


def SeeClients (verifi):
    if verifi == True:
        print("Usted puede ver la lista de los clientes")
    else:
        print("Usted no puede ver la lista de los clientes")



nombre  = input("Escribe el nombre: ")
archivo = open("BD.txt","a")
archivo.write(nombre+"\t")
archivo.close()

apellido  = input("Escribe el Apellido: ")
archivo = open("BD.txt","a")
archivo.write(apellido+"\t")
archivo.write("\n")
archivo.close()

a = np.loadtxt('BD.txt',dtype=str)

cols = 2
row_labels = []
column_labels = ['Nombre','Apellido']
print("\n")
#Row count function
def row_count():
    e = 0 #Elementos del array totales
    f = 0 #Filas del Array
    for row in a:
        for elem in row:
            e = e+1
        f = f+1  
    #Establecer Columnas con un for
    #row_labels = [] #Se empieza un array vacio para llenarlo con nueva info
    cont = 1 #Contador del while son las filas que hay
    while cont < f+1:
        row_labels.append(cont) #Agregar la fila numero x al array
        cont = cont+1
    #column_labels = ['C1','C2']
    df = pd.DataFrame(a,columns=column_labels,index=row_labels)
    print(df)
row_count()