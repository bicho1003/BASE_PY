class Rectangulo:

    def __init__(self):
        self.b = 10
        self.h = 10

    def area(self):
        print("El area es: " + str(self.b*self.h))

class Usuario:
    def __init__(self,see,add,delete,modify,list):
        self.see = see
        self.add = add
        self.delete = delete
        self.modify = modify
        self.list = list
    
    def Clientadd(self):
        if self.add == True:
            print("Usted puede agregar lo que quiera")
        else:
            print("Usted no puede agregar nada")

    def Clientdelete(self):
        if self.delete == True:
            print("Usted puede borrar lo que quiera")
        else:
            print("Usted no puede borrar nada")

    def Clientmodify(self):
        if self.delete == True:
            print("Usted puede modificar lo que quiera")
        else:
            print("Usted no puede modififcar nada")

    def Clientlist(self):
        if self.delete == True:
            print("Usted puede enlistar lo que quiera")
        else:
            print("Usted no puede enlistar nada")

class Admin(Usuario(True,True,True,True,True)):
    def whoami():
        print("Soy un admin")

class Gerente(Usuario(False,True,True,True,True)):
    def whoami():
         print("Soy un Gerente")

