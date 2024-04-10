"""
# Angel Daniel Solano Meza 372453
# Examen 2 

calificaciones = 0
total = 0
aprobados = 0
reprobados = 0
calificacion = int(input("Ingrese la calificacion, -1 para terminar: "))
while calificacion < -1 or calificacion > 100:
        print("La calificacion esta fuera de rango, ingrese una entre el 1 y 100")
        calificacion = int(input("Ingrese la calificacion, -1 para terminar: "))
if calificacion != -1:
    total = total + 1
    calificaciones = calificaciones + calificacion;
    if calificacion >= 60:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
else:
    calificaciones = -1
while calificacion != -1:
    calificacion = int(input("Ingrese la calificacion, -1 para terminar: "))
    while calificacion < -1 or calificacion > 100:
        print("La calificacion esta fuera del rango establecido, por favor ingrese una calificacion entre  y 100")
        calificacion = int(input("Ingrese la calificacion, -1 para terminar: "))
    if calificacion != -1:
        calificaciones = calificaciones + calificacion;
        total = total + 1
        if calificacion >= 60:
            aprobados = aprobados + 1
        else:
            reprobados = reprobados + 1
        
if calificaciones == -1:
    print("No se ingresaron calificaciones")
else:
    promedio = calificaciones / total
    print(f"Promedio de calificaciones capturadas del segundo examen parcial: {promedio:.0f}")
    print("Cantidad de alumnos aprobados en el segundo examen parcial: ",aprobados)
    print("Cantidad de alumnos reprobados en el segundo examen parcial: ",reprobados)
    print("El docente obtuvo un buen desempeño en el segundo parcial." if promedio >= 90 else "El docente no obtuvo un buen desmpeño en el segundo examen parcial")

longitud = int(input('Ingrese un número impar para establecer la longitud horizontal de la base del triangulo: '))
caracter = input('Ingrese el carácter que imprimirá el triángulo: ')

cadena_triangulo = ''
numero_espacio = longitud // 2
numero_caracter = 1 

for renglon_parte1 in range (longitud // 2):
    columna = 0
    numero_caracteres_renglon = numero_espacio + numero_caracter

    for columna in range(numero_caracteres_renglon):
        if columna < numero_espacio:
            cadena_triangulo += ' '
        else:
            cadena_triangulo = cadena_triangulo + caracter
    
    numero_caracter = numero_caracter + 2
    numero_espacio = numero_espacio - 1
    cadena_triangulo = cadena_triangulo + '\n'

for renglon_parte2 in range(longitud):
    cadena_triangulo = cadena_triangulo + caracter

cadena_triangulo = cadena_triangulo + '\n'

print(cadena_triangulo)
"""
numero = 9
base = numero
for base in range(numero, 0, -1):
    for cero in range(numero, 0, -1):
        print("0", end="")
    print()
    