
import unittest
from src.jugador import jugador
class TestJugador(unittest.TestCase):
    def test_creacion_jugador(self):
        j = jugador("Lautaro", "X")
        self.assertEqual(j.nombre, "Lautaro")
        self.assertEqual(j.ficha, "X")

    def test_nombre_no_vacio(self):
        j = jugador("Facundo", "O")
        self.assertNotEqual(j.nombre, "")

    def test_ficha_valida_x(self):
        j = jugador("Player1", "X")
        self.assertIn(j.ficha, ["X", "O"])

    def test_ficha_valida_o(self):
        j = jugador("Player2", "O")
        self.assertIn(j.ficha, ["X", "O"])

    def test_dos_jugadores_diferentes(self):
        j1 = jugador("Jugador1", "X")
        j2 = jugador("Jugador2", "O")
        self.assertNotEqual(j1.nombre, j2.nombre)
        self.assertNotEqual(j1.ficha, j2.ficha)

    def test_jugador_tiene_nombre_tipo_str(self):
        j = jugador("Ana", "X")
        self.assertIsInstance(j.nombre, str)

    def test_jugador_tiene_ficha_tipo_str(self):
        j = jugador("Tomi", "O")
        self.assertIsInstance(j.ficha, str)

    def test_nombre_con_espacios(self):
        j = jugador("Juan Perez", "X")
        self.assertEqual(j.nombre, "Juan Perez")

    def test_ficha_minuscula_convertida(self):
        j = jugador("Beto", "x".upper())
        self.assertEqual(j.ficha, "X")

    def test_nombre_con_caracteres_especiales(self):
        j = jugador("L@u#t@ro!", "X")
        self.assertEqual(j.nombre, "L@u#t@ro!")

if __name__ == "__main__":
    unittest.main()