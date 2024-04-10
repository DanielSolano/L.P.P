horas = "Horas"
num_bacterias = "Numero de bacterias"
bact = 200
tiempo = 0
bactN = 0

print(horas, "\t", num_bacterias, sep="")
for i in range(5):
    print(tiempo, "\t", bactN, sep="")
    tiempo += 5
    bactN = 200 * 2 ** tiempo

print("")
tiempo = 0
bactN = 0
for i in range(5):
    print(f"{horas:>5} {num_bacterias:>25}")
    print(f"{tiempo:>0} {bactN:>28}")
    tiempo += 5
    bactN = 200 * 2 ** tiempo

tiempo_1 = int(input("Ingrese una cantidad de tiempo en segundos: "))

horas_1 = tiempo_1 // 3600
tiempo_1 = tiempo_1 % 3600 
minutos_1 = tiempo_1 // 60
segundos_1 = tiempo_1 % 60

print(horas_1, minutos_1, segundos_1, sep="-")

tiempo_2 = int(input("Ingrese una cantidad de tiempo en segundos: "))

horas_2 = tiempo_2 // 3600
sobrante = tiempo_2 % 3600
minutos_2 = sobrante // 60
segundos_2 = sobrante % 60

print("Horas:", horas_2, "Minutos:", minutos_2, "Segundos:", segundos_2)

numero = int(input("Ingrese un numero entero: "))
suma = 0

for i in range(1, numero):
    if numero % i == 0:
        suma += i

print("El numero", numero, "", end="")
if suma == numero:
    print("es perfecto")
else:
    print("es imperfecto")

numero_binario_1 = int(input("Ingrese un numero binario: " ))
numero_binario_original = numero_binario_1

numero_decimal_1 = 0
posicion_1 = 0
while numero_binario_1 > 0:
    digito_1 = numero_binario_1 % 10
    numero_decimal_1 += digito_1 * (2 ** posicion_1)
    numero_binario_1 //= 10
    posicion_1 += 1

print("El numero binario", numero_binario_original, "es equivalente en decimal a", numero_decimal_1)

numero_decimal_2 = int(input("Ingrese un numero binario: "))
numero_decimal_original = numero_decimal_2
numero_binario_2 = 0
posicion_2 = 1
while numero_decimal_2 > 0:
    digito_binario_2 = numero_decimal_2 % 2
    numero_binario_2 += digito_binario_2 * posicion_2
    numero_decimal_2 //= 2
    posicion_2 *= 10

print("El numero decimal", numero_decimal_original, "es equivalente en binario a", numero_binario_2)

numero_1 = int(input("Ingrese un numero para determinar si es capicua: "))
reverso_1 = 0
numero_original_1 = numero_1

while numero_1 > 0:
    digito_1 = numero_1 % 10
    reverso_1 = reverso_1 * 10 + digito_1
    numero_1 //= 10

if reverso_1 == numero_original_1:
    print("El numero es capicua")
else:
    print("El numero no es capicua")

print()
texto_usuario_1 = input("Ingrese una oracion para determinar si es palindromo: ")

texto_1 = ''
for caracter in texto_usuario_1:
    if 'A' <= caracter <= 'Z':
        caracter = chr(ord(caracter) + 32) 
    texto_1 += caracter

texto_sin_especiales_1 = ''
for caracter in texto_1:
    if 'a' <= caracter <= 'z' or '0' <= caracter <= '9':
        texto_sin_especiales_1 += caracter

texto_invertido_1 = ''
for i in range(len(texto_sin_especiales_1) - 1, -1, -1):
    texto_invertido_1 += texto_sin_especiales_1[i]

if texto_sin_especiales_1 == texto_invertido_1:
    print("El texto ingresado es un palíndromo")
else:
    print("El texto ingresado no es un palíndromo")
