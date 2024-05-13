import random



def generaLista(o1, o2, o3):
    lista = []
    numero = random.randint(1,9)
    for i in range(o1):
        if elementoRepetido(numero, lista):
            lista.append(numero)
            numero = random.randint(1,9)
        else:
            numero = random.randint(1,9)
            while not elementoRepetido(numero, lista):
                numero = random.randint(1,9)
            lista.append(numero) 
    
    numero = random.randint(10,19)        
    for i in range(o2):
        if elementoRepetido(numero, lista):
            lista.append(numero)
            numero = random.randint(10,19)
        else:
            numero = random.randint(10,19)
            while not elementoRepetido(numero, lista):
                numero = random.randint(10,19)
            lista.append(numero) 
    
    numero = random.randint(20,28)
    for i in range(o3):
        if elementoRepetido(numero, lista):
            lista.append(numero)
            numero = random.randint(20,28)
        else:
            numero = random.randint(20,28)
            while not elementoRepetido(numero, lista):
                numero = random.randint(20,28)
            lista.append(numero) 
            
    lista = sorted(lista)    
    return lista

def elementoRepetido(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return False
    return True

def listaRepetida(lista, listas):
    for i in range(len(listas)):
        if listas[i] == lista:
            return False
    return True

def escribirListasTXT(nombre, listas):
    f = open(nombre, "w")
    for lista in listas:
        for elemento in lista:
            f.write(f'{elemento} ')
        f.write("\n")
    f.close()   

def leerTXT(archivo):
    listas = []
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            lista = []
            for elemento in linea.split(' '):
                if elemento != '\n':
                    lista.append(int(elemento))
            listas.append(lista)
    return listas

def afortunados(premiada):
    ganadores = []
    listas = leerTXT("listas.txt")
    print(listas)
    for boleto in range(len(listas)):
        aciertos = 0
        lista = sorted(listas[boleto])
        for numero in range(5):
            if premiada[numero] == lista[numero]:
                aciertos += 1
        ganadores.append(aciertos)
    return sorted(ganadores)

listas = []
lista = []

# GENERAR LISTAS

for i in range(1000):
    lista = generaLista(2,2,1)
    while not listaRepetida(lista, listas):
        lista = generaLista(2,2,1)
    listas.append(lista)

# ORDENAR LISTAS

listas = sorted(listas)

# ESCRIBIR LISTAS EN TXT

escribirListasTXT("listas.txt", listas)

afortunado = []
afortunado.append(int(input(f'Ingrese el 1er. numero ganador: ')))
afortunado.append(int(input(f'Ingrese el 2do. numero ganador: ')))
afortunado.append(int(input(f'Ingrese el 3er. numero ganador: ')))
afortunado.append(int(input(f'Ingrese el 4to. numero ganador: ')))
afortunado.append(int(input(f'Ingrese el 5to. numero ganador: ')))
afortunado = sorted(afortunado)

# GANADORES

ganadores = afortunados(afortunado)
print(f'Para el numero afortunado {afortunado}')
print(f'Ganadores con 2 aciertos: {ganadores.count(2)}')
print(f'Ganadores con 3 aciertos: {ganadores.count(3)}')
print(f'Ganadores con 4 aciertos: {ganadores.count(4)}')
print(f'Ganadores con 5 aciertos: {ganadores.count(5)}')

    
    