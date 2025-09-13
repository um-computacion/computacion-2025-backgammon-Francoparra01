from core.tablero.tablero import Tablero
from core.jugador.jugador import Jugador
from core.dados.dados import Dados

class Juego:
    def __init__(self, jugador1: Jugador, jugador2: Jugador):
        self.tablero = Tablero()
        self.jugadores = [jugador1, jugador2]
        self.turno_idx = 0
        self.dados = Dados()

    def jugador_actual(self) -> Jugador:
        return self.jugadores[self.turno_idx]

    def cambiar_turno(self):
        self.turno_idx = 1 - self.turno_idx

    def tirar_dados(self) -> list[int]:
        d1, d2 = self.dados.tirar()
        return self.dados.expandir(d1, d2)

