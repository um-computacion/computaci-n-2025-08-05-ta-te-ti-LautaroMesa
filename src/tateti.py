"""
from src.tablero import Tablero
class PosicionInvalidaError(Exception):
    pass
class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.tablero = Tablero()
        self.turno = jugador1

    def cambiar_turno(self):
        self.turno = self.jugador1 if self.turno == self.jugador2 else self.jugador2

    def jugar_turno(self, posicion):
        self.tablero.colocar_ficha(posicion, self.turno.ficha)
        if self.tablero.hay_ganador(self.turno.ficha):
            return 'ganador'
        elif self.tablero.esta_lleno():
            return 'empate'
        else:
            self.cambiar_turno()
            return 'continuar'
"""
from src.tablero import Tablero,PosicionInvalidaError, CasillaOcupadaError

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.tablero = Tablero()
        self.turno = jugador1

    def cambiar_turno(self):
        self.turno = self.jugador1 if self.turno == self.jugador2 else self.jugador2

    def jugar_turno(self, posicion):
        self.tablero.colocar_ficha(posicion, self.turno.ficha)
        if self.tablero.hay_ganador(self.turno.ficha):
            return 'ganador'
        if self.tablero.esta_lleno():
            return 'empate'
        self.cambiar_turno()
        return 'continuar'