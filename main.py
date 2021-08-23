import mymodule


def main():
    print("Hola mundo")
    persona1 = mymodule.Usuario("1","Daniel","Alberto","Ayala","Dominguez","328092489023")
    print ("\n" + str(persona1) + "\n")
    print(persona1.tostr())
    rect = mymodule.Rectangulo()
    rect.area()


main()