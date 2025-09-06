from core.jugador.jugador import Jugador

def test_jugador_basico():
    j = Jugador("Alice", "blanco", 1)
    assert j.nombre() == "Alice"
    assert j.color() == "blanco"
    assert j.direccion() == 1

def test_jugador_negro():
    j = Jugador("Bob", "negro", -1)
    assert j.nombre() == "Bob"
    assert j.color() == "negro"
    assert j.direccion() == -1
