# carta.py
"""Clase Carta que representan una carta de juego y su nombre de archivo de imagen."""

class Carta:
    CARAS = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']
    PALOS = ['Corazones', 'Diamantes', 'Tréboles', 'Espadas']
    
    def __init__(self, cara, palo):
        """Inicializar una Carta con una cara y un palo."""
        self._cara = cara
        self._palo = palo
        
    @property
    def cara(self):
        """Devuelve el valor self._cara de la carta"""
        return self._cara
    
    @property
    def palo(self):
        """Devuelve el valor self._palo de la carta"""
        return self._palo
    
    @property
    def nombre_de_imagen(self):
        """Devuelve el nombre del archivo de la imagen de la carta"""
        return str(self).replace(' ', '_') + '.png'
    
    def __repr__(self):
        """Devuelve la representación de cadena para repr()."""
        return f"Carta(cara='{self.cara}', palo='{self.palo}')"
    
    def __str__(self):
        """Devuelve la representación de cadena para str()."""
        return f'{self.cara} de {self.palo}'
    
    def __format__(self, formato):
        """Devuelve la representación de cadena formateada para str()."""
        return f'{str(self):{formato}}'
    
    
