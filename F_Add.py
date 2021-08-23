import pandas as pd 
import numpy as np

#Cargar BD.txt
a = np.loadtxt('BD.txt',dtype=str)
print(a)
#Contar filas del Array
cols = 2
row_labels = []
column_labels = ['C1','C2']
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
row_count()
#Mostrar DataFrame
print("Base de Datos Actual")
df = pd.DataFrame(a,columns=column_labels,index=row_labels)
print(df)
print("\n")
###Funcion Agregar###
a2 = []
row_labels = []
def row_add():
    a = np.loadtxt('BD.txt',dtype=str)
    #row_count()
    new = 0
    while new < cols:
        C1 = input("Nuevo valor: ")
        a2.append(C1)
        new = new+1
    #a = np.append(a,a2,axis=0)#No son de la misma dimension #Numpy solution to append
    #a = np.concatenate((a,[a2]),axis=0,)
    a = np.vstack((a,a2))
    ##RowCount_Begin
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
        ##RowCount_End
    df = pd.DataFrame(a, columns=column_labels,index=row_labels)
    print(df)
row_add()
#row_count()
#Mostrar DF
#df = pd.DataFrame(a, columns=column_labels,index=row_labels)
#print(df)