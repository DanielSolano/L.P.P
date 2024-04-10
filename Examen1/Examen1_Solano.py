# Solano Meza Angel Daniel
# Parte 1
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

iguales = 0
salida = 0
if num1 == num2 == num3:
    iguales = 1

if iguales == 1:
    print('Los valores',num1, num2,'y',num3,'son iguales')
    print('Todos los numeros son iguales, por lo tanto no es necesario mostrar su ordenamiento')
if iguales == 0:
    print('Los valores',num1, num2,'y',num3,'no son iguales')
    if (num1 >= num2 >= num3): 
        if salida == 0:
            print('El orden de los numeros de forma descendente son:',num1, num2,'y',num3)
        salida = 1
    if (num1 >= num3 >= num2): 
        if salida == 0:
            print('El orden de los numeros de forma descendente son:',num1, num3,'y',num2)
        salida = 1
    if (num2 >= num1 >= num3): 
        if salida == 0:       
            print('El orden de los numeros de forma descendente son:',num2, num1,'y',num3)
        salida = 1
    if (num1 <= num2 <= num3):
        if salida == 0:
            print('El orden de los numeros de forma descendente son:',num3, num2,'y',num1)
        salida = 1
    if (num1 <= num2 >= num3):
        if salida == 0:
            print('El orden de los numeros de forma descendente son:',num2, num3,'y',num1)
        salida = 1
    if (num1 >= num2 <= num3):
        if salida == 0:
            print('El orden de los numeros de forma descendente son:',num3, num1,'y',num2)
        salida = 1

# Parte 2

huevos_obtenidos = int(input("Ingresar la cantidad de huevos obtenidos: "))
huevos_por_cartera = 6

carteras_llenas = huevos_obtenidos // huevos_por_cartera
huevos_restantes = huevos_obtenidos % huevos_por_cartera

huevos_adicionales = 0

if huevos_restantes > 0:
    huevos_adicionales = huevos_por_cartera - huevos_restantes

if carteras_llenas >= 1:
    print(f"Se llenaron {carteras_llenas} carteras de {huevos_por_cartera} huevos.")

if huevos_restantes:
    print(f"En la ultima cartera se colococaron {huevos_restantes} huevos.")

if huevos_adicionales >= 1:
    print(f"La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de: {huevos_adicionales}.")

if huevos_obtenidos % 6 != 0:
    print('La cantidad de huevos que se necesitan para llenar una cartera es de:',6-huevos_adicionales)
