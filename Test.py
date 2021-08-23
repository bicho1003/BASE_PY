import pandas as pd
import numpy as np

###Para guardar en BD.txt ###
a = [
    ['a','b']
    ]
#Contar filas del array
cols = 2
row_labels = []
column_labels = ['C1','C2']
#Funcion contar
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
row_count()
df = pd.DataFrame(a,columns=column_labels,index=row_labels)
print(df)
a2 = []
print(a)
def row_add():
    row_count()
    new = 0
    while new < cols:
        C1 = input("C1: ")
        a2.append(C1)
        new = new+1
    a.append(a2)
row_add()
print(a)