# core/tablero/test_tablero.py
import pytest
from core.tablero.tablero import Tablero

def test_inicializacion_tablero_estado_basico():
    t = Tablero()

    # ACCESO CORRECTO (sin name mangling)
    agujas = t.__agujas__

    assert len(agujas) == 24
    assert all(isinstance(x, tuple) and isinstance(x[0], str) and isinstance(x[1], int) for x in agujas)

    esperadas = {
        0:  ("blanco", 2),
        11: ("blanco", 5),
        16: ("blanco", 3),
        18: ("blanco", 5),
        23: ("negro", 2),
        12: ("negro", 5),
        7:  ("negro", 3),
        5:  ("negro", 5),
    }
    for idx, valor in esperadas.items():
        assert agujas[idx] == valor

    for i in range(24):
        if i not in esperadas:
            assert agujas[i] == ("ninguno", 0)

def test_inicializacion_cuenta_total_de_fichas():
    t = Tablero()
    agujas = t.__agujas__

    total_blancas = sum(n for c, n in agujas if c == "blanco")
    total_negras  = sum(n for c, n in agujas if c == "negro")

    assert total_blancas == 15
    assert total_negras  == 15

def test_barra_y_retirada_inician_en_cero():
    t = Tablero()
    assert t.__barra__    == {"blanco": 0, "negro": 0}
    assert t.__retirada__ == {"blanco": 0, "negro": 0}
