import sys

# Ejercicio 9

print(ord('B'),ord('C'),ord('D'),ord('b'),ord('c'),ord('d'),ord('0'),ord('1'),ord('2'),ord('$'),ord('*'),ord('+'))

# Ejercicio 10

n1 = int(input('Ingrese el primer numero:'))
n2 = int(input('Ingrese el segundo numero:'))
n3 = int(input('Ingrese el tercer numero:'))

print('La suma de',n1,'+',n2,'+',n3,'es:',(n1+n2+n3))
print('El promedio de los numeros',n1,'+',n2,'+',n3,'es:',(n1+n2+n3)/3)
print('El producto de los numeros',n1,'*',n2,'*',n3,'es:',(n1*n2*n3))

mayor = n1
if(n2 > mayor):
    mayor = n2
if (n3 > mayor):
    mayor = n3

menor = n1
if(n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3

print('El mayor de los numeros',n1,n2,n3,'es:',mayor)
print('El menor de los numeros',n1,n2,n3,'es:',menor)

# Ejercicio 11

numero = int(input('Ingrese un numero de 5 digitos:'))

print(numero // 10000, numero // 1000 % 10, numero // 100 % 10, numero // 10 % 10, numero // 1 % 10)

# Ejercicio 12

capital = 100000
rendimiento = 0.07  
n = 10
dinero_total = capital*(1 + rendimiento)**n
print('Dinero total a 10 anios',dinero_total)
n = 20
dinero_total = capital*(1 + rendimiento)**n
print('Dinero total a 20 anios',dinero_total)
n = 30
dinero_total = capital*(1 + rendimiento)**n
print('Dinero total a 30 anios',dinero_total)

# Ejercicio 13

# numero = 2 ** 14285
sys.set_int_max_str_digits(100000)
# print(numero)

# Si utilizamos una exponenciacion mayor a 12484 no podemos imprimir la cadena ya que python solo permite la conversion de enteros a cadenas  4300 caracteres
# si ingresamos un entero mayor debemos de utilizar la funcion sys.set_int_max_str_digits(100000) para cambiar el maximo permitido y poder imprimirlo

# Ejercicio 14

digito = int(input('Ingrese un numero y te dire su ultimo digito:'))
print('El ultimo digito del numero',digito,'es:',(digito % 10))

# Ejercicio 15


num1 = int(input('Ingrese el primer numero:'))
num2 = int(input('Ingrese el segundo numero:'))
num3 = int(input('Ingrese el tercer numero:'))

menor2 = num1
if(num2 < menor2):
    menor2 = num2
if (num3 < menor2):
    menor2 = num3

print('El menor de los numeros',num1,num2,num3,'es:',menor2)

# Ejercicios 16

num1 = int(input('Ingrese el primer numero:'))
num2 = int(input('Ingrese el segundo numero:'))
num3 = int(input('Ingrese el tercer numero:'))

if (num1 == num2):
    if (num2==num3):
       print('Los numeros',num1,num2,num3,'son iguales')
    if (num2 != num3):
        print('Los numeros',num1,num2,num3,'no son iguales')

if (num1 != num2):
    if (num2 != num3):
        print('Los numeros',num1,num2,num3,'no son iguales')
    if (num2 == num3):
       print('Los numeros',num1,num2,num3,'no son iguales')

# Ejercicio 17

num1 = int(input('Ingrese el primer numero:'))
num2 = int(input('Ingrese el segundo numero:'))
num3 = int(input('Ingrese el tercer numero:'))

if num1 <= num2:
    if num2 <= num3:
        print(f"El orden de los números de forma ascendente son: {num1}, {num2}, {num3}")
    if num3 < num2:
        if num1 <= num3:
            print(f"El orden de los números de forma ascendente son: {num1}, {num3}, {num2}")
        if num3 < num1:
            print(f"El orden de los números de forma ascendente son: {num3}, {num1}, {num2}")

if num2 < num1:
    if num1 <= num3:
        print(f"El orden de los números de forma ascendente son: {num2}, {num1}, {num3}")
    if num3 < num1:
        if num2 <= num3:
            print(f"El orden de los números de forma ascendente son: {num2}, {num3}, {num1}")
        if num3 < num2:
            print(f"El orden de los números de forma ascendente son: {num3}, {num2}, {num1}")

# Cartera de huevos

huevos_obtenidos = int(input("Ingresar la cantidad de huevos obtenidos: "))
huevos_por_cartera = int(input("La cantidad de huevos que se necesitan para llenar una cartera es de: "))

carteras_llenas = huevos_obtenidos // huevos_por_cartera
huevos_restantes = huevos_obtenidos % huevos_por_cartera

huevos_adicionales = 0
if huevos_restantes > 0:
    huevos_adicionales = huevos_por_cartera - huevos_restantes

if carteras_llenas >= 1:
    print(f"Se llenaron {carteras_llenas} carteras de {huevos_por_cartera} huevos.")

if huevos_restantes == 1:
    print(f"En la ultima cartera se coloco {huevos_restantes} huevo.")
if huevos_restantes > 1:
    print(f"En la ultima cartera se colocaron {huevos_restantes} huevos.")

if huevos_adicionales >= 1:
    print(f"La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de: {huevos_adicionales}.")

