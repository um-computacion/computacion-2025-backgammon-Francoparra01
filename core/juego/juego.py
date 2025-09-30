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

    def mover_ficha(self, desde: int, hasta: int, color: str):
        c_desde, n_desde = self.tablero._Tablero__agujas__[desde]
        assert c_desde == color and n_desde > 0, "No hay ficha del color en 'desde'"

        c_hasta, n_hasta = self.tablero._Tablero__agujas__[hasta]

        if c_hasta in ("ninguno", color):
            self.tablero._Tablero__agujas__[hasta] = (color, n_hasta + 1)
        else:
            if n_hasta == 1:
                self.tablero._Tablero__barra__[c_hasta] += 1
                self.tablero._Tablero__agujas__[hasta] = (color, 1)
            else:
                raise ValueError("Movimiento inválido: aguja bloqueada por rival")

        if n_desde == 1:
            self.tablero._Tablero__agujas__[desde] = ("ninguno", 0)
        else:
            self.tablero._Tablero__agujas__[desde] = (color, n_desde - 1)

    def estado_juego(self) -> dict:
        return {
            "jugador_actual": self.jugador_actual().nombre(),
            "barra": dict(self.tablero._Tablero__barra__),
            "retirada": dict(self.tablero._Tablero__retirada__),
        }



    

    
