
# Creacion de una tupla vacia

tupla = ()

# Creacion de una tupla con elementos

tupla2 = 'a', 'b', 1, 3, '#'
tupla3 = ('a', 'b', 1, 3, '#')

# Creacion de una tupla con un solo elemento

tupla4 = 1,
tupla5 = (1,)

tupla = ('a', 'b', 'd')
tupla[0]  # Primer elemento de la tupla. 'a'
tupla[1]  # Segundo elemento de la tupla. 'b'

bebidas = ('agua', 'café', 'batido', 'sorbete')
bebidas[-1] # Ultimo elemento de la tupla. 'sorbete'
bebidas[-3] # Tercer elemento de la tupla. 'café'

vocales = 'a', 'e', 'i', 'o', 'u'

subconjunto = vocales[2:3]  # Elementos desde el índice 2 hasta el índice 3-1
              # Salida ('i',)
              
subconjuto2 = vocales[2:4]  # Elementos desde el 2 hasta el índice 4-1
              # ('i', 'o')
              
subconjunto3 = vocales[:]    # Todos los elementos
              # Salida ('a', 'e', 'i', 'o', 'u')

subconjunto4 = vocales[1:]  # Elementos desde el índice 1
             # ('e', 'i', 'o', 'u')
             
subconjunto5 = vocales[:3]  # Elementos hasta el índice 3-1
             # Salida ('a', 'e', 'i')

# Inmutabilidad

# mi_tupla = ("hola", "mundo", "!")
# mi_tupla[1] = "planeta"

# Añadimos elementos al final

alFinal = vocales + ('x', 'y', 'z')  

# Añadimos elementos al principio

vocales = ('x', 'y', 'z') + vocales

# Añadimos elementos al final

vocales =  vocales + ('x', 'y', 'z') 

# Añadimos elementos en una posición específica

vocales = vocales[:3] + ('b', 'c') + vocales[3:]

# Añadimos elementos en una posición específica

n = 2
tupla = (12 , 34, 45, 22, 33 )
tupla[ : n]
tupla[n : ]
tupla = tupla[ : n ] + (19 ,) + tupla[n : ]

# Añadir una tupla a una lista

tupla = (12 , 34, 45, 22, 33 )
lista = [10, "Adios"]
lista.append(tupla)
# Salida [10, 'Adios', (12, 34, 45, 22, 33)]
tupla2 = lista[2][2]
print(tupla2)
# Salida = 45

# Añadir una lista a una tupla

# contenido de la lista = [10, 'Adios', (12, 34, 19, 45, 22, 33)]

tupla = 10, "Adios", lista
print(tupla)
# Salida (10, 'Adios', [10, 'Adios', (12, 34, 19, 45, 22, 33)])

lista[2] = 100
print(tupla)
# Salida (10, 'Adios', [10, 'Adios', 100])

# Desembalaje de tuplas

# Tupla (10, 'Adios', [10, 'Adios', 100])

numero, despido, otra_lista = tupla

# numero = 10
# despido = 'Adios'
# otra_lista = [10, 'Adios', 100]

# Intercambiando de valores

a = 5
b = 10
# Se crea una tupla temporal con (10, 5)
a, b = b, a 

# a, b = 10, 5

# Usar enumarate()

tupla = ("manzana", "pera", "naranja")
for indice, fruta in enumerate(tupla):
  print(f"Índice: {indice}, Fruta: {fruta}")
  
# Índice: 0, Fruta: manzana
# Índice: 1, Fruta: pera
# Índice: 2, Fruta: naranja

# Obteniendo subconjunto de inicio a fin

mi_tupla = ("hola", "mundo", "!")
tupla_cortada = mi_tupla[:]  # Equivalente a mi_tupla[0:len(mi_tupla)]
# Salida: ('hola', 'mundo', '!')

# Obtener un subconjunto desde el segundo elemento hasta el final

mi_tupla = ("hola", "mundo", "!")
tupla_cortada = mi_tupla[1:]
# Salida: ('mundo', '!')

# Obtener un subconjunto invertido

mi_tupla = ("hola", "mundo", "!")
tupla_cortada = mi_tupla[::-1]
# Salida: ('!', 'mundo', 'hola')


# Pasar una tupla a una funcion

def calcular_total(productos, impuesto, costo_envio):
  total_productos = sum(productos)
  impuesto_aplicado = total_productos * (impuesto / 100)
  costo_total = total_productos + impuesto_aplicado + costo_envio
  return costo_total

# Ejemplo de uso
precios_productos = (25.99, 12.95, 5.49)  # Tupla de precios
porcentaje_impuesto = 10  # Impuesto en porcentaje
costo_envio = 3.50

costo_compra = calcular_total(precios_productos, porcentaje_impuesto, costo_envio)
print(f"Costo total: ${costo_compra:.2f}")  # Salida: Costo total: $52.37

"""
  Calcula el costo total de una compra.

  Args:
    productos: Tupla con precios de productos.
    impuesto: Porcentaje de impuesto a aplicar.
    costo_envio: Costo fijo de envío.

  Returns:
    Costo total de la compra (incluyendo impuesto y envío).
  """
  
