import unittest
from src.tablero import Tablero
from src.tateti import Tateti, PosicionInvalidaError
from src.jugador import jugador

class TestTateti(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.jugador1 = jugador("Ana", "X")
        self.jugador2 = jugador("Luis", "O") 
        self.tateti = Tateti(self.jugador1, self.jugador2)
    
    # Tests para __init__
    def test_inicializacion_con_jugadores(self):
        """Test que el juego se inicializa correctamente con dos jugadores"""
        self.assertEqual(self.tateti.jugador1, self.jugador1)
        self.assertEqual(self.tateti.jugador2, self.jugador2)
        self.assertEqual(self.tateti.turno, self.jugador1)  # Empieza jugador1
        self.assertIsInstance(self.tateti.tablero, Tablero)
    
    def test_turno_inicial_es_jugador1(self):
        """Test que el turno inicial es del jugador1"""
        self.assertEqual(self.tateti.turno, self.jugador1)
    
    # Tests para cambiar_turno()
    def test_cambiar_turno_de_jugador1_a_jugador2(self):
        """Test cambiar turno cuando es turno del jugador1"""
        self.tateti.turno = self.jugador1
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, self.jugador2)
    
    def test_cambiar_turno_de_jugador2_a_jugador1(self):
        """Test cambiar turno cuando es turno del jugador2"""
        self.tateti.turno = self.jugador2
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, self.jugador1)
    
    def test_cambiar_turno_multiple_veces(self):
        """Test cambiar turno múltiples veces alterna correctamente"""
        # Inicial: jugador1
        self.assertEqual(self.tateti.turno, self.jugador1)
        
        # 1er cambio: jugador2
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, self.jugador2)
        
        # 2do cambio: jugador1
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, self.jugador1)
        
        # 3er cambio: jugador2
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, self.jugador2)
    
    # Tests para jugar_turno()
    def test_jugar_turno_continuar(self):
        """Test jugar turno que permite continuar el juego"""
        resultado = self.tateti.jugar_turno(0)
        self.assertEqual(resultado, 'continuar')
        # Verifica que se colocó la ficha
        self.assertEqual(self.tateti.tablero.casillas[0], 'X')
        # Verifica que cambió el turno
        self.assertEqual(self.tateti.turno, self.jugador2)
    
    def test_jugar_turno_ganador_jugador1(self):
        """Test jugar turno donde jugador1 gana"""
        # Preparar tablero casi ganado por jugador1
        self.tateti.tablero.casillas = ['X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ']
        
        resultado = self.tateti.jugar_turno(2)  # Completa la fila superior
        self.assertEqual(resultado, 'ganador')
        self.assertEqual(self.tateti.tablero.casillas[2], 'X')
        # El turno NO debe cambiar cuando hay ganador
        self.assertEqual(self.tateti.turno, self.jugador1)
    
    def test_jugar_turno_ganador_jugador2(self):
        """Test jugar turno donde jugador2 gana"""
        # Cambiar al turno del jugador2
        self.tateti.turno = self.jugador2
        # Preparar tablero casi ganado por jugador2
        self.tateti.tablero.casillas = ['X', 'X', ' ', 'O', 'O', ' ', 'X', ' ', ' ']
        
        resultado = self.tateti.jugar_turno(5)  # Completa la fila media
        self.assertEqual(resultado, 'ganador')
        self.assertEqual(self.tateti.tablero.casillas[5], 'O')
        self.assertEqual(self.tateti.turno, self.jugador2)
    
    def test_jugar_turno_empate(self):
        """Test jugar turno que resulta en empate"""
        # Preparar tablero casi lleno sin ganador
        self.tateti.tablero.casillas = ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', ' ']
        # Última jugada en la posición 8 (poner 'O' para que no haya ganador)
        self.tateti.turno = self.jugador2  # Asegura que le toca a O
        resultado = self.tateti.jugar_turno(8)
        self.assertEqual(resultado, 'empate')
        self.assertEqual(self.tateti.tablero.casillas[8], 'O')
        self.assertEqual(self.tateti.turno, self.jugador2)

    def test_juego_completo_empate(self):
        """Test de un juego completo que termina en empate"""
        movimientos = [
            (0, 'continuar'),  # X
            (1, 'continuar'),  # O
            (2, 'continuar'),  # X
            (5, 'continuar'),  # O
            (3, 'continuar'),  # X
            (6, 'continuar'),  # O
            (4, 'continuar'),  # X
            (8, 'continuar'),  # O
            (7, 'empate')      # X
        ]
        self.tateti = Tateti(self.jugador1, self.jugador2)
        for posicion, resultado_esperado in movimientos:
            resultado = self.tateti.jugar_turno(posicion)
            self.assertEqual(resultado, resultado_esperado)
    
    def test_estado_tablero_despues_varios_movimientos(self):
        """Test que el estado del tablero es correcto después de varios movimientos"""
        self.tateti.jugar_turno(0)  # X
        self.tateti.jugar_turno(4)  # O
        self.tateti.jugar_turno(1)  # X
        
        esperado = ['X', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(self.tateti.tablero.casillas, esperado)
        self.assertEqual(self.tateti.turno, self.jugador2) 
    
    # Tests de casos límite
    def test_verificar_ganador_todas_combinaciones(self):
        """Test verificar que se detecta ganador en todas las combinaciones posibles"""
        combinaciones_ganadoras = [
            # Filas
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columnas  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonales
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combinacion in combinaciones_ganadoras:
            # Reiniciar juego
            tateti_temp = Tateti(self.jugador1, self.jugador2)
            
            # Simular movimientos para que jugador1 esté a punto de ganar
            for i, pos in enumerate(combinacion[:-1]):
                tateti_temp.tablero.casillas[pos] = 'X'
                if i < len(combinacion) - 2:
                    tateti_temp.cambiar_turno()
                    for libre in range(9):
                        if libre not in combinacion and tateti_temp.tablero.casillas[libre] == ' ':
                            tateti_temp.tablero.casillas[libre] = 'O'
                            break   
                    tateti_temp.cambiar_turno()
                    
            resultado = tateti_temp.jugar_turno(combinacion[-1])
            self.assertEqual(resultado, 'ganador', 
                           f"No detectó ganador en combinación {combinacion}")


class TestPosicionInvalidaError(unittest.TestCase):
    """Tests para la excepción personalizada"""
    
    def test_posicion_invalida_error_es_excepcion(self):
        """Test que PosicionInvalidaError hereda de Exception"""
        self.assertTrue(issubclass(PosicionInvalidaError, Exception))
    
    def test_posicion_invalida_error_con_mensaje(self):
        """Test que se puede crear la excepción con mensaje"""
        mensaje = "Posición inválida"
        error = PosicionInvalidaError(mensaje)
        self.assertEqual(str(error), mensaje)


if __name__ == '__main__':
    unittest.main(verbosity=2)