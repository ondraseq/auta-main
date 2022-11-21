from auta import Auta

def test_atributy():
    a = Auta("Skoda", "Fabia", "2L", "Modra")
    assert a.vyrobce == "Skoda"
    assert a.model == "Fabia"
    assert a.objem == "2L"
    assert a.barva == "Modra"