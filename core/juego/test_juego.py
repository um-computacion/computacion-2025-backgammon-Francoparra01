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

def test_mover_ficha_blanco_simple():
    j1 = Jugador("Agus", "blanco", 1)
    j2 = Jugador("Fran", "negro", -1)
    juego = Juego(j1, j2)

    # Antes de mover
    color, cant = juego.tablero._Tablero__agujas__[0]
    assert color == "blanco" and cant == 2

    # Mover ficha blanca de 0 a 1
    juego.mover_ficha(0, 1, "blanco")

    # Aguja 0 pierde una ficha
    assert juego.tablero._Tablero__agujas__[0][1] == 1
    # Aguja 1 ahora tiene 1 ficha blanca
    assert juego.tablero._Tablero__agujas__[1] == ("blanco", 1)

def test_mover_ficha_captura():
    j1 = Jugador("Agus", "blanco", 1)
    j2 = Jugador("Fran", "negro", -1)
    juego = Juego(j1, j2)

    # Colocar manualmente 1 ficha negra en aguja 1
    juego.tablero._Tablero__agujas__[1] = ("negro", 1)

    # Mover ficha blanca de 0 a 1 → debería capturar
    juego.mover_ficha(0, 1, "blanco")

    # Aguja 1 queda con una ficha blanca
    assert juego.tablero._Tablero__agujas__[1] == ("blanco", 1)
    # La ficha negra va a la barra
    assert juego.tablero._Tablero__barra__["negro"] == 1

