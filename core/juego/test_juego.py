import pytest
from core.jugador.jugador import Jugador
from core.juego.juego import Juego

def test_juego_inicializacion():
    j1 = Jugador("Agus", "blanco", 1)
    j2 = Jugador("Fran", "negro", -1)
    juego = Juego(j1, j2)

    assert juego.jugador_actual().nombre() == "Agus"
    assert len(juego.jugadores) == 2

def test_cambiar_turno():
    j1 = Jugador("Agus", "blanco", 1)
    j2 = Jugador("Fran", "negro", -1)
    juego = Juego(j1, j2)

    assert juego.jugador_actual().nombre() == "Agus"
    juego.cambiar_turno()
    assert juego.jugador_actual().nombre() == "Fran"
