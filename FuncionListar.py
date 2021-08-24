import numpy as np
import pandas as pd

a = np.loadtxt('BD.txt',dtype=str)

#Contar filas del array
e = 0 #Elementos del array totales
f = 0 #Filas del Array
for row in a:
    for elem in row:
       e = e+1
    f = f+1   
#Establecer Columnas con un for
row_labels = [] #Se empieza un array vacio para llenarlo con nueva info
cont = 1 #Contador del while son las filas que hay
while cont < f+1:
    row_labels.append(cont) #Agregar la fila numero x al array
    cont = cont+1
column_labels = ['Nombre','Apellido']
"""#Mosrtar el arreglo
for row in a:
    for elem in row:
        print(elem,end='\t')
    print()
"""
#Mostrar el arreglo con columnas numero de fila
df = pd.DataFrame(a,columns=column_labels,index=row_labels)
print(df)