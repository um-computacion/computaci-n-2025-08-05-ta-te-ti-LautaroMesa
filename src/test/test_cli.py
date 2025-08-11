
import unittest
from src.cli import CLIParaTest


class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
import sys
sys.modules['jugador'] = sys.modules[__name__]

class TestCLIParaTest(unittest.TestCase):

    def test_jugador_gana_horizontal(self):
        entradas = [
            "Lautaro",  
            "Facundo", 
            "0",  
            "3", 
            "1", 
            "4", 
            "2"  
        ]
        cli = CLIParaTest(entradas)
        cli.iniciar()
        self.assertIn("¡Lautaro ganó!", cli.salida)

    def test_empate(self):
        entradas = [
            "Lautaro", "Facundo",
            "0", "1", "2",
            "4", "3", "5",
            "7", "6", "8"
        ]
        cli = CLIParaTest(entradas)
        cli.iniciar()
        self.assertIn("¡Empate!", cli.salida)

    def test_error_valor_no_entero(self):
        entradas = ["L1", "L2", "a", "0", "1", "2", "3", "4", "5", "6", "7", "8"]
        cli = CLIParaTest(entradas)
        cli.iniciar()
        errores = [s for s in cli.salida if "Error" in s]
        self.assertTrue(any("número entero" in e for e in errores))

    def test_error_posicion_invalida(self):
        entradas = ["J1", "J2", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8"]
        cli = CLIParaTest(entradas)
        cli.iniciar()
        errores = [s for s in cli.salida if "Error" in s]
        self.assertTrue(any("no es válida" in e for e in errores))

    def test_error_casilla_ocupada(self):
        entradas = ["J1", "J2", "0", "0", "1", "2", "3", "4", "5", "6", "7", "8"]
        cli = CLIParaTest(entradas)
        cli.iniciar()
        errores = [s for s in cli.salida if "Error" in s]
        self.assertTrue(any("ya está ocupada" in e for e in errores))

if __name__ == '__main__':
    unittest.main()
