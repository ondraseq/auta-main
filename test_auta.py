from auta import Auta

def test_atributy():
    a = Auta("Skoda", "Fabia", "2L", "Modra")
    assert a.vyrobce == "Skoda"
    assert a.model == "Fabia"
    assert a.objem == "2L"
    assert a.barva == "Modra"

def test_equal():
    a1 = Auta("Skoda", "Fabia", "2L", "Modra")
    a2 = Auta("Skoda", "Fabia", "2L", "Modra")
    assert a1 == a2