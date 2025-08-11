from src.jugador import jugador
from src.tateti import Tateti
from src.tablero import PosicionInvalidaError, CasillaOcupadaError
class CLIParaTest:
    def __init__(self, entradas):
        self.entradas = entradas
        self.salida = []

    def input(self, prompt=""):
        if self.entradas:
            return self.entradas.pop(0)
        return ""

    def print(self, mensaje):
        self.salida.append(mensaje)

    def iniciar(self):
        self.print("BIENVENIDOS A MI TATETÍ")
        nombre1 = self.input("Nombre del Jugador 1 (X): ")
        nombre2 = self.input("Nombre del Jugador 2 (O): ")

        jugador1 = jugador(nombre1, 'X')
        jugador2 = jugador(nombre2, 'O')
        juego = Tateti(jugador1, jugador2)
        while True:
            # No mostramos el tablero real, solo simulamos
            self.print(f"\nTurno de {juego.turno.nombre} ({juego.turno.ficha})")
            try:
                pos = int(self.input("Elige una posición (0-8): "))
                estado = juego.jugar_turno(pos)
            except ValueError:
                self.print("Error: Debes ingresar un número entero.")
                continue
            except PosicionInvalidaError as e:
                self.print(f"Error: {e}")
                continue
            except CasillaOcupadaError as e:
                self.print(f"Error: {e}")
                continue

            if estado == 'ganador':
                self.print(f"¡{juego.turno.nombre} ganó!")
                break
            elif estado == 'empate':
                self.print("¡Empate!")
                break
class CLI:
    def iniciar(self):
        print("BIENVENIDOS A MI TATETÍ")
        nombre1 = input("Nombre del Jugador 1 (X): ")
        nombre2 = input("Nombre del Jugador 2 (O): ")

        jugador1 = jugador(nombre1, 'X')
        jugador2 = jugador(nombre2, 'O')
        juego = Tateti(jugador1, jugador2)

        while True:
            juego.tablero.mostrar()
            print(f"\nTurno de {juego.turno.nombre} ({juego.turno.ficha})")

            try:
                pos = int(input("Elige una posición (0-8): "))
                estado = juego.jugar_turno(pos)
            except ValueError:
                print("Error: Debes ingresar un número entero.")
                continue
            except PosicionInvalidaError as e:
                print(f"Error: {e}")
                continue
            except CasillaOcupadaError as e:
                print(f"Error: {e}")
                continue

            if estado == 'ganador':
                juego.tablero.mostrar()
                print(f"¡{juego.turno.nombre} ganó!")
                break
            elif estado == 'empate':
                juego.tablero.mostrar()
                print("¡Empate!")
                break
if __name__ == "__main__":
    cli = CLI()
    cli.iniciar()