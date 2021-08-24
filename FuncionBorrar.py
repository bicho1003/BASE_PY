import pandas as pd
import numpy as np

#Cargar la BD.tx al array
a = np.loadtxt('BD.txt',dtype=str)
#Contar las filas que hay para el data frame
e = 0
f = 0
for row in a:
    for elem in row:
        e = e+1
    f = f+1
row_labels = []
cont = 1
while cont < f+1:
    row_labels.append(cont)
    cont = cont+1
column_labels = ['Nombre','Apellido']
#Hacer un data DataFrame
df = pd.DataFrame(a,columns=column_labels,index=row_labels)
print(df)
print("\n")
match = int(input("Que fila quieres borrar?: "))


#Borra la fila con indice x (Especificado por el usuario)
print("\n")
b = np.delete(a,match-1,axis=0)
print("Fila borrada: "+ str(match)+"\n")
#Volver a contar filas y mostrar nueva BD
e=0#Inicializar e y f
f=0
for row in b:
    for elem in row:
        e = e+1
    f = f+1
row_labels = []
cont = 1
while cont < f+1:
    row_labels.append(cont)
    cont = cont+1
column_labels = ['Nombre','Apellido']
##Guardar nueva BD en BD.txt
newarray = np.savetxt("BD.txt",b,fmt='%s')#%s es el codigo de un string

#Nuevo DataFrame de b
print("Nueva Base de Datos: \n")
dfb = pd.DataFrame(b,columns=column_labels,index=row_labels)
print(dfb)
print("\n")



