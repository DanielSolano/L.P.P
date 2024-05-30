from baraja import BarajaDeCartas
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Primer ejemplo
# baraja_de_cartas = BarajaDeCartas()
# print(baraja_de_cartas)
# baraja_de_cartas.barajar()
# print(baraja_de_cartas)

# print(baraja_de_cartas.repartir_carta())



#Segundo ejemplo
baraja_de_cartas = BarajaDeCartas()
#%matplotlib
from pathlib import Path
path = Path('.').joinpath('imagenes_de_cartas')


(figura, lista_de_ejes) = plt.subplots(nrows=4, ncols=13)


for ejes in lista_de_ejes.ravel():
    ejes.get_xaxis().set_visible(False)
    ejes.get_yaxis().set_visible(False)
    nombre_de_imagen = baraja_de_cartas.repartir_carta().nombre_de_imagen
    img = mpimg.imread(str(path.joinpath(nombre_de_imagen).resolve()))
    ejes.imshow(img)

# figura.tight_layout()
# plt.show()


baraja_de_cartas.barajar()

for ejes in lista_de_ejes.ravel():
    ejes.get_xaxis().set_visible(False)
    ejes.get_yaxis().set_visible(False)
    nombre_de_imagen = baraja_de_cartas.repartir_carta().nombre_de_imagen
    img = mpimg.imread(str(path.joinpath(nombre_de_imagen).resolve()))
    ejes.imshow(img)

# figura.tight_layout()
plt.show()