# Angel Daniel Solano Meza

i = 1
print("\n")
while i <= 5:
    print(i)
    i += 1

i = 5
print("\n")
while i >= 1:
    print(i)
    i -= 1
print("\n")

i = 1
while i <= 5:
    if i != 5:
        print(i, end=", ")
    if i == 5:
        print(i)
    i += 1
print("\n")

i = 5
while i >= 1:
    if i != 1:
        print(i, end=", ")
    if i == 1:
        print(i)
    i -= 1
print("\n")

numero = int(input("Ingrese un numero entero para calcular su sumatoria: "))
i = numero
suma = 0
while i >= 0 :
    suma += numero - i
    i -= 1

print('La sumatoria de', numero, 'es', suma)
print("\n")

renglon = 0
maximo_renglon = 10
maximo_columna = 16
cadena_renglon_columna = ''

while renglon < maximo_renglon:
    columna = 0
    while columna < maximo_columna:
        cadena_renglon_columna += '❤️' + ' '
        columna += 1
    cadena_renglon_columna += '\n'
    renglon += 1
print(cadena_renglon_columna)
print("\n")

nombre = str(input("Ingrese su nombre: "))
char = str(input("Ingrese un caracter: "))

i = len(nombre) + 1
while i >= 0:
    if (i != 0):
        print(char, end="")
    if (i == 0):
        print(char)
    i -= 1 
print(char, end='')
print(nombre, end='') 
print(char, end='\n')
i = len(nombre) + 1
while i >= 0:
    print(char, end="")
    i -= 1
print("\n")

longitud = int(input("Ingrese un número impar para establecer la longitud horizontal más larga del rombo: "))
caracter = input("Ingrese el carácter que tendrá el rombo: ")

i = 1
medio = int(longitud / 2)

while i < longitud:
    blank = ' ' * medio
    print(f"{blank}{caracter * i}{blank}")
    medio -= 1
    i += 2

while i > 0:
    blank = ' ' * medio
    print(f"{blank}{caracter * i}{blank}")
    medio += 1
    i -= 2

