import os

articulos = []
listaCompras = []
articulosComprados = []

with open("Exposiciones\inventario.txt", "r") as archivo:
    for linea in archivo:
        articulos.append(linea[:-1].upper())

del articulos[0]

with open("Exposiciones\Lista de compras.txt", "r") as archivo:
    for linea in archivo:
        listaCompras.append(linea[:-1].upper())

print(listaCompras)
canidadArticulos = len(listaCompras)

while len(articulosComprados) < 10:
    for i in range(len(articulos)):
        print(f"{i + 1}- {articulos[i]}")

    articulo = input("Articulo a eliminar: ").upper()

    if articulo in articulos:
        articulos.remove(articulo)
        articulosComprados.append(articulo)
        print("Articulo comprado")
    else:
        print("Articulo no encontrado")

    input("Presiona enter para continuar...")

if articulosComprados == listaCompras:
    print("Lista de compras completada")
else:
    print("Articulos de la lista no comprados")