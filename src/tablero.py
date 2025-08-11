class PosicionInvalidaError(Exception):
    pass

class CasillaOcupadaError(Exception):
    pass

class Tablero:
    def __init__(self):
        self.casillas = [' ' for _ in range(9)]

    def mostrar(self):
        for i in range(3):
            print(" | ".join(self.casillas[i*3:(i+1)*3]))
            if i < 2:
                print("--+---+--")

    def colocar_ficha(self, posicion, ficha):
        if not (0 <= posicion <= 8):
            raise PosicionInvalidaError(f"La posición {posicion} no es válida. Debe ser entre 0 y 8.")
        if self.casillas[posicion] != ' ':
            raise CasillaOcupadaError(f"La casilla {posicion} ya está ocupada.")
        self.casillas[posicion] = ficha

    def hay_ganador(self, ficha):
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(self.casillas[i] == self.casillas[j] == self.casillas[k] == ficha for i, j, k in combinaciones)

    def esta_lleno(self):
        return ' ' not in self.casillas

