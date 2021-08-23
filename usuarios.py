import SysFunc


class Rectangulo:

    def __init__(self):
        self.b = 10
        self.h = 10

    def area(self):
        print("El area es: " + str(self.b*self.h))

class Usuario():
    """Clase Principal usuario"""
    """Constructor de la clase Usuario"""
    def __init__(self,idusuario,pnombre,snombre,papellido,sapellido,rfc):
        self.idusuario = idusuario
        self.Pnombre = pnombre
        self.Snombre = snombre
        self.Papellido = papellido
        self.Sapellido = sapellido
        self.Rfc = rfc

    """Funcion que permite imprimer los atributos en pantalla"""
    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return "%s, %s %s, %s, %s, %s." % (
            self.idusuario, self.Pnombre, self.Snombre, 
            self.Papellido, self.Papellido,self.Rfc)
    
    """Funci[on que permite convertir sus atribuos en una LISTA"""
    def tostr(self):
        objstr = [self.idusuario, self.Pnombre, self.Snombre, 
            self.Papellido, self.Papellido,self.Rfc]
        return objstr
    
class Cliente(Usuario):
    """Esta es una clase que tiene la info de cada cliente representa a los clientes"""
    """Constructor de la clase Cliente"""
    def __init__(self,idusuario,pnombre,snombre,papellido,sapellido,rfc,razonsoc,telefono,correo):
        """Contrcutor de la clase padre (Usuario)"""
        super.__init__(self,idusuario,pnombre,snombre,papellido,sapellido,rfc)

        """ Atribuitos de la clase Cliente"""
        self.RazonSoc = razonsoc
        self.Telefono = telefono
        self.Correo = correo

class Admin(Usuario):
    """Esta clase tiene todos los permisos para realizar cualquier acci[on dentro del programa"""
    """Contructor de la Clase ADMIN"""
    def __init__(self, idusuario, pnombre, snombre, papellido, sapellido, rfc):
        """Constructor de la clase padre (Usuario) utilizando "Super" el cual llama a su constructor """
        super().__init__(idusuario, pnombre, snombre, papellido, sapellido, rfc)
        """Atributos de la clase Admin"""
        self.See = True
        self.Add = True
        self.Del = True
        self.Mod = True
        self.Lis = True
        






    """" Constructor de la clase admin
    def __init__(self,see,add,delete,modify,list):
        self.see = see
        self.add = add
        self.delete = delete
        self.modify = modify
        self.list = list
    """
    """  Funciones de Clase ADministrador y Gerente
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
    """
"""class Admin(Usuario(True,True,True,True,True)):
    def whoami():
        print("Soy un admin")

class Gerente(Usuario(False,True,True,True,True)):
    def whoami():
         print("Soy un Gerente")
"""
