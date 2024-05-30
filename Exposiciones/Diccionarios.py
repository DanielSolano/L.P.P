def AgregarEstudiante(estudiantes):
    id = input("Ingrese el número de identificación: ")
    nombre = input("Ingrese el nombre completo: ")
    edad = int(input("Ingrese la edad: "))
    print("Estudiante agregado")
    estudiantes[id] = {"Nombre": nombre, "Edad": edad}

def BuscarEstudiante(estudiantes):
    id = input("Ingrese el número de identificación: ")
    if id in estudiantes:
        print("Nombre: ", estudiantes[id]["Nombre"])
        print("Edad: ", estudiantes[id]["Edad"])
    else:
        print("Estudiante no encontrado")

def MostrarEstudiantes(estudiantes):
    for id in estudiantes:
        print("ID: ", id)
        print("Nombre: ", estudiantes[id]["Nombre"])
        print("Edad: ", estudiantes[id]["Edad"])

def EliminarEstudiante(estudiantes):
    id = input("Ingrese el número de identificación: ")
    if id in estudiantes:
        del estudiantes[id]
        print("Estudiante eliminado")
    else:
        print("Estudiante no encontrado")

op = 0
estudiantes = {}
while op != 5:
    input("\nPresione Enter para continuar...")
    print("----------------------------------------")
    print("\nMenu")
    print("1. Agregar un Estudiante")
    print("2. Buscar un Estudiante por Número de Identificación")
    print("3. Mostrar Todos los Estudiantes Registrados")
    print("4. Eliminar un Estudiante")
    print("5. Salir")
    op = int(input("Ingrese una opción: "))
    print("----------------------------------------")
    if op == 1:
        AgregarEstudiante(estudiantes)
    elif op == 2:
        BuscarEstudiante(estudiantes)
    elif op == 3:
        MostrarEstudiantes(estudiantes)
    elif op == 4:
        EliminarEstudiante(estudiantes)
    elif op == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")
