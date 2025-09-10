import pytest
from core.jugador.jugador import Jugador
from core.tablero.tablero import Tablero

def test_jugador_atributos_basicos():
    j = Jugador("Agus", "blanco", 1)
    assert j.nombre() == "Agus"
    assert j.color() == "blanco"
    assert j.direccion() == 1
    assert "Agus" in str(j)   # chequea __str__

def test_fichas_totales_iniciales():
    t = Tablero()
    j_blanco = Jugador("Agus", "blanco", 1)
    j_negro = Jugador("Fran", "negro", -1)

    assert j_blanco.fichas_totales(t) == 15
    assert j_negro.fichas_totales(t) == 15

def test_tiene_en_barra():
    t = Tablero()
    j_blanco = Jugador("Agus", "blanco", 1)

    # al incio no hay fichas en barra
    assert not j_blanco.tiene_en_barra(t)

    # simulacion fichas en barra
    t._Tablero__barra__["blanco"] = 2
    assert j_blanco.tiene_en_barra(t)

