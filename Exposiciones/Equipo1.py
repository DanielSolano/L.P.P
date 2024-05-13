import random

def lanzar_dado():
    dados = (random.randint(1, 6) ,  random.randint(1, 6))
    return dados

def mostrar_dado(dados):
    print("Dados:",dados[0], dados[1])
    
saldo = 1000
print("Tu saldo inicial es de $1000")
print("¿Deseas lanzar o retirarte?")
entrada= ("lanzar", "retirar")
decision= input()
if (decision == "retirar"):
    print("Tu saldo final es de:",saldo)
    exit()
elif (decision == "lanzar"):
    apuesta = int(input("¿Cuánto deseas apostar?: "))
    while apuesta > saldo:
        print("No tienes suficiente saldo")
        apuesta = int(input("¿Cuánto deseas apostar?: "))
    saldo -= apuesta
    tirada = lanzar_dado()
    mostrar_dado(tirada)
    if sum(tirada) == 7 or sum(tirada) == 11:
        print("Ganaste")
        print("Tu saldo final es de:",saldo + apuesta * 2)
    elif sum(tirada) == 2 or sum(tirada) == 3 or sum(tirada) == 12:
        print("Perdiste")
        print("Tu saldo final es de:",saldo)
    else:
           
            while tirada != 7 and saldo > 0:
                print("Tu saldo es de:",saldo)
                print("Puedes seguir jugando")
                print("¿Deseas lanzar o retirarte?")
                entrada= ("lanzar", "retirar")
                decision= input()
                if (decision == "retirar"):
                    print("Tu saldo final es de:",saldo)
                    exit()
                elif (decision == "lanzar"):
                    apuesta = int(input("¿Cuánto deseas apostar?"))
                    while apuesta > saldo:
                        print("No tienes suficiente saldo")
                        apuesta = int(input("¿Cuánto deseas apostar?: "))
                    saldo -= apuesta
                    tirada = lanzar_dado()
                    mostrar_dado(tirada)
                    if sum(tirada) == 7:
                        print("Perdiste")
                        print("Tu saldo final es de:",saldo)
                        break
                    elif sum(tirada) == tirada:
                        print("Ganaste")
                        print("Tu saldo final es de:",saldo + apuesta * 2) 
                        break
                    else:
                        continue