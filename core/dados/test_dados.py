import pytest
from core.dados.dados import Dados
import random

def test_tirar_rango_basico():
    d = Dados()
    for _ in range(50):
        a, b = d.tirar()
        assert 1 <= a <= 6
        assert 1 <= b <= 6

def test_tirar_con_seed_es_reproducible():
    rng = random.Random(123)
    d = Dados(rng)
    
    assert d.tirar() == (1, 3)   
    assert d.tirar() == (1, 4)

def test_expandir_no_dobles():
    assert Dados.expandir(2, 5) == [2, 5]

def test_expandir_dobles():
    assert Dados.expandir(3, 3) == [3, 3, 3, 3]
