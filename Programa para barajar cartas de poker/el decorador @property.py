# En Python, el decorador @property es una forma de definir métodos que se comportan
# como atributos, lo que permite controlar el acceso a los atributos de una clase.
# El uso de @property proporciona una manera de encapsular el acceso a los atributos,
# permitiendo definir getters, setters y deleters de una manera limpia y pythonica.

# Uso de @property
# El decorador @property se utiliza para definir un método que actúa como un getter, 
# lo que permite acceder a un atributo como si fuera una propiedad normal,
# pero con la capacidad de incluir lógica adicional si es necesario.

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting value")
        self._temperature = value

    @temperature.deleter
    def temperature(self):
        print("Deleting value")
        del self._temperature

# Uso de la clase Celsius
c = Celsius()
c.temperature = 37  # Invoca el setter
print(c.temperature)  # Invoca el getter
del c.temperature  # Invoca el deleter


# Beneficios de Usar @property

# Encapsulamiento:
#     Proporciona una forma de proteger el acceso a los atributos internos de una clase.
#     Permite agregar lógica adicional cuando se accede o se modifica un atributo.
    
# Interfaz Limpia:
#     Permite acceder a métodos como si fueran atributos, 
#haciendo el código más limpio y fácil de leer.

# Compatibilidad hacia Adelante:
#     Si decides cambiar la implementación interna de un atributo, 
#puedes hacerlo sin cambiar la interfaz pública de la clase.