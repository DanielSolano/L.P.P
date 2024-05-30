# baraja.py
"""La clase Baraja representa una baraja de cartas."""
import random
from carta import Carta

class BarajaDeCartas:
    NUMERO_DE_CARTAS = 52 # constante del número de cartas
    
    def __init__(self):
        """Inicializa el mazo o la baraja."""
        self._carta_actual = 0
        self._baraja = []
        
        for cuenta in range(BarajaDeCartas.NUMERO_DE_CARTAS):
            self._baraja.append(Carta(Carta.CARAS[cuenta % 13], Carta.PALOS[cuenta // 13]))
            
    def barajar(self):
        """Barajar el mazo"""
        self._carta_actual = 0
        random.shuffle(self._baraja)
        
    def repartir_carta(self):
        """Regresa una carta."""
        try:
            carta = self._baraja[self._carta_actual]
            self._carta_actual += 1
            return carta
        except:
            return None
        
    def __str__(self):
        """Devuelve una representación de cadena en _baraja actual."""
        s = ''
        
        for índice, carta in enumerate(self._baraja):
            s += f'{self._baraja[índice]:<19}'
            if (índice + 1) % 4 == 0:
                s += '\n'
                
        return s
    
