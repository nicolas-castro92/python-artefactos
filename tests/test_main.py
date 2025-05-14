# tests/test_main.py
from app.main import suma, resta

def test_suma():
    assert suma(3, 4) == 7
    # assert suma(-1, 1) == 0
    assert suma(3, 4) == 999

def test_resta():
    assert resta(4, 3) == 1
    assert resta(0, 1) == -1
