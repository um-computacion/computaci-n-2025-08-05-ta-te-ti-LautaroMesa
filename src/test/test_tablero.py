
import unittest
from src.tablero import Tablero, PosicionInvalidaError, CasillaOcupadaError
class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_vacio(self):
        self.assertEqual(self.tablero.casillas, [' '] * 9)

    def test_colocar_ficha_correctamente(self):
        self.tablero.colocar_ficha(0, 'X')
        self.assertEqual(self.tablero.casillas[0], 'X')

    def test_colocar_ficha_posicion_invalida_negativa(self):
        with self.assertRaises(PosicionInvalidaError):
            self.tablero.colocar_ficha(-1, 'X')

    def test_colocar_ficha_posicion_invalida_mayor(self):
        with self.assertRaises(PosicionInvalidaError):
            self.tablero.colocar_ficha(9, 'X')

    def test_colocar_ficha_en_posicion_ocupada(self):
        self.tablero.colocar_ficha(0, 'X')
        with self.assertRaises(CasillaOcupadaError):
            self.tablero.colocar_ficha(0, 'O')

    def test_hay_ganador_horizontal(self):
        self.tablero.casillas = ['X', 'X', 'X',
                                 ' ', ' ', ' ',
                                 ' ', ' ', ' ']
        self.assertTrue(self.tablero.hay_ganador('X'))

    def test_hay_ganador_vertical(self):
        self.tablero.casillas = ['O', ' ', ' ',
                                 'O', ' ', ' ',
                                 'O', ' ', ' ']
        self.assertTrue(self.tablero.hay_ganador('O'))

    def test_hay_ganador_diagonal(self):
        self.tablero.casillas = ['X', ' ', ' ',
                                 ' ', 'X', ' ',
                                 ' ', ' ', 'X']
        self.assertTrue(self.tablero.hay_ganador('X'))

    def test_no_hay_ganador(self):
        self.tablero.casillas = ['X', 'O', 'X',
                                 'X', 'O', 'O',
                                 'O', 'X', 'O']
        self.assertFalse(self.tablero.hay_ganador('X'))

    def test_esta_lleno_true(self):
        self.tablero.casillas = ['X', 'O', 'X',
                                 'X', 'O', 'O',
                                 'O', 'X', 'O']
        self.assertTrue(self.tablero.esta_lleno())

    def test_esta_lleno_false(self):
        self.tablero.casillas = ['X', 'O', 'X',
                                 ' ', 'O', 'O',
                                 'O', 'X', 'O']
        self.assertFalse(self.tablero.esta_lleno())

if __name__ == '__main__':
    unittest.main()

