"""
# Inicializacion de variables
total = 0
contador = 0
calificacion = int(input("Ingrese la calificacion del alumno: (-1 para dejar de ingresar calificaciones)"))
if calificacion == -1:
    print("No se ingresaron calificaciones.")
else:
    while calificacion != -1:
        total = total + calificacion
        contador += 1
        calificacion = int(input("Ingrese otra calificacion de alumno:(-1 para dejar de ingresar calificaciones) "))
    promedio = total / contador
    print (f"El promedio de calificaciones es: {promedio}")
"""

"""
reprobados = 0
aprobados = 0
for contador in range(10):
    alumno = int(input(f"Alumno {contador + 1}: "))
    if alumno >= 60:
        aprobados += 1
    else:
        reprobados += 1
    contador += 1
print(f"El total de aprobados es: {aprobados}")
print(f"El total de reprobados es: {reprobados}")
if aprobados >= 8:
    print("Bonificacion otorgada al docente")
else:
    print("No se otorga bonificacion al docente")
"""
"""
for repetecion in range(2):
    numero = int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    repetecion += 1
"""

for i in range(99, -1, -11):
    print(i);

i = 0
suma = 0
for i in range(2, 101, 2):
    suma += i
    
print(suma)