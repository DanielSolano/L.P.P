import os, re

# Ejercicio exposicion

def agregar_estudiante():
    identificacion = input("Ingrese el numero de identificacion del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    estudiantes[identificacion] = {"nombre": nombre, "edad" : edad}
    print("Estudiante agregado con exito")

def buscar_estudiante():
    identificacion = input("Ingrese el numero de identificacion del estudiante: ")
    if identificacion in estudiantes:
        print(f"Nombre: {estudiantes[identificacion]['nombre']}")
    else:
        print("Estudiante no encontrado")

def mostrar_estudiantes():
    valores = estudiantes.items()
    print(valores)
    for matricula, estudiante, in estudiantes.items():
        print(f"Matricula: {matricula}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
    
def eliminar_estudiante():
    identificacion = input("Ingrese el numero de identificacion del estudiante: ")
    if identificacion in estudiantes:
        del estudiantes[identificacion]
        print("Estudiante eliminado con exito")
    else:
        print("Estudiante no encontrado")

estudiantes = {}
opcion = -1
while opcion != 0:
    print("1. Agregar un estudiante")
    print("2. Buscar un estudiante por un numero de identificacion")
    print("3. Mostrar los estudiantes registrados")
    print("4. Eliminar un estudiante")
    print("0. Salir")
    opcion = int(input("Ingrese una opcion: "))
    os.system("cls")
    if opcion == 1:
        agregar_estudiante()
        os.system("pause")
        os.system("cls")
    elif opcion == 2:
        buscar_estudiante()
        os.system("pause")
        os.system("cls")
    elif opcion == 3:
        mostrar_estudiantes()
        os.system("pause")
        os.system("cls")
    elif opcion == 4:
        eliminar_estudiante()
        os.system("pause")
        os.system("cls")
    elif opcion == 0:
        print("Saliendo...")
        os.system("pause")
        os.system("cls")

# Ejercicio 1

palabras = {}
cadena = input("Ingrese una oracion para determinar el numero de palabras unicas en ella:  ")
split = cadena.split(" ")
for i in split:
    if i in palabras.keys():
        palabras[i] = {'cantidad' : palabras[i]['cantidad'] + 1}
    else:
        palabras[i] = {'cantidad' : 1}

print(f"PALABRA  CANTIDAD ")
for palabra, numero in palabras.items():
    print(f"{palabra:<8} {numero['cantidad']:<7}")
    
print(f'Numero de palabras unicas: {len(palabras)}')


def leer_combinaciones(archivo):
    numeros = {}

    with open(archivo, 'r') as file:
        for idx, linea in enumerate(file, start=1):
            grupos = linea.strip().split()

            for i, grupo in enumerate(grupos, start=1):
                combinaciones = numeros.setdefault(f'Grupo {i}', {})
                combinacion = ' '.join(grupo.split()[:5]) 
                combinaciones[combinacion] = combinaciones.get(combinacion, 0) + 1

    return numeros

#Ejercicio 3

palabras = {}
cadena = input("Ingrese una oracion para determinar el numero de palabras unicas en ella: ")

# Eliminar caracteres especiales usando expresiones regulares
split = re.findall(r'\b\w+\b', cadena.lower())

for palabra in split:
    if palabra in palabras:
        palabras[palabra] = {'cantidad': palabras[palabra]['cantidad'] + 1}
    else:
        palabras[palabra] = {'cantidad': 1}

print("PALABRA  CANTIDAD")
for palabra, datos in palabras.items():
    print(f"{palabra:<8} {datos['cantidad']:<7}")

print(f'Numero de palabras unicas: {len(palabras)}')
