# core/tablero/test_tablero.py
import pytest
from core.tablero.tablero import Tablero

def test_inicializacion_tablero_estado_basico():
    t = Tablero()
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

def test_estado_aguja_devuelve_tupla_correcta():
    t = Tablero()
    assert isinstance(t.estado_aguja(0), tuple)
    assert t.estado_aguja(0) == ("blanco", 2)
    assert t.estado_aguja(7) == ("negro", 3)

def test_getters_barra_y_retirada():
    t = Tablero()
    assert t.fichas_en_barra("blanco") == 0
    assert t.fichas_retiradas("negro") == 0

    t.__barra__["blanco"] = 2
    t.__retirada__["negro"] = 5

    assert t.fichas_en_barra("blanco") == 2
    assert t.fichas_retiradas("negro") == 5

def test_total_fichas_suma_todas_las_fuentes():
    t = Tablero()
    assert t.total_fichas("blanco") == 15
    assert t.total_fichas("negro") == 15

    t.__barra__["blanco"] = 1
    t.__retirada__["blanco"] = 2

    c18, n18 = t.__agujas__[18]
    t.__agujas__[18] = (c18, n18 - 2)
    c11, n11 = t.__agujas__[11]
    t.__agujas__[11] = (c11, n11 - 1)

    assert t.total_fichas("blanco") == 15

def test_aguja_vacia_true_y_false():
    t = Tablero()
    t.__agujas__[3] = ("ninguno", 0)
    t.__agujas__[4] = ("blanco", 1)

    assert t.aguja_vacia(3) is True
    assert t.aguja_vacia(4) is False

def test_mostrar_tablero_imprime_formato_basico(capsys):
    t = Tablero()
    t.mostrar_tablero()
    out = capsys.readouterr().out

    assert "Aguja  0:" in out
    assert "Barra:" in out
    assert "Retiradas:" in out

