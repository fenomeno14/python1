def selec_menu():
    print("                                       ")
    print("                                       ")
    print("*** NOMINA ACME ***")
    print("        MENU")
    print("1- Agregar empleado")
    print("2- Modificar empleado")
    print("3- Buscar empleado")
    print("4- Eliminar empleado")
    print("5- Listar empleados")
    print("6- Listar nómina de un empleado")
    print("7- Listar nómina de todos los empleados")
    print("8- Salir")
    print(">> Escoja una opción (1-8)?")
    while True:
        
        seleccion = int(input("Elija una opcion: "))
        if seleccion == 1:
           Agregar_empleado ()
        if seleccion == 2:
            modificar_empleado ()

idemp = []
nombres = []
num_horas = []
val_horas = []
def Agregar_empleado ():
    print("Agregar empleado")
    while True:
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre == "fin":
            selec_menu()
        idem = int(input("Ingrese el Id del empleado: "))
        num_h = input("Ingrese el numero de horas trabajadas por el empleado: ")
        valor = input("Ingrese el valor de las horas trabajadas por el empleado: ")
        idemp.append(idem)
      
        nombres.append(nombre)
        
        num_horas.append(num_h)
        
        val_horas.append(valor)

        print(idemp)
        print(nombres)
        print(num_horas)
        print(val_horas)

def modificar_empleado ():
    print("Modificar empleado")        
           
selec_menu()


