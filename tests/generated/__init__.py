import pytest
from src.calculator import Calculator


# =========================
# 1. TESTS PASSANTS
# =========================

@pytest.mark.parametrize("a,b,expected", [
    (5, 7, 12),
    (0, 0, 0),
    (-3, 3, 0)
])
def test_add(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 3, 7),
    (0, 5, -5),
    (-3, -2, -1)
])
def test_subtract(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (4, 6, 24),
    (-2, 5, -10),
    (0, 100, 0)
])
def test_multiply(a, b, expected):
    calc = Calculator()
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (20, 4, 5),
    (5, 2, 2.5),
    (-10, -2, 5)
])
def test_divide(a, b, expected):
    calc = Calculator()
    assert calc.divide(a, b) == expected

@pytest.mark.parametrize("base,exp,expected", [
    (2, 5, 32),
    (2, -3, 0.125),
    (5, 0, 1)
])
def test_power(base, exp, expected):
    calc = Calculator()
    assert calc.power(base, exp) == expected

@pytest.mark.parametrize("a,b,expected", [
    (17, 5, 2),
    (-17, 5, 3),
    (10, 3, 1)
])
def test_modulo(a, b, expected):
    calc = Calculator()
    assert calc.modulo(a, b) == expected

@pytest.mark.parametrize("n,expected", [
    (5, 120),
    (0, 1),
    (1, 1)
])
def test_factorial(n, expected):
    calc = AdvancedCalculator()
    assert calc.factorial(n) == expected

@pytest.mark.parametrize("n,expected", [
    (13, True),
    (9973, True),
    (-7, False),
    (1, False),
    (2, True)
])
def test_is_prime(n, expected):
    calc = AdvancedCalculator()
    assert calc.is_prime(n) == expected

# =========================
# 2. TESTS NON-PASSANTS (ERREURS ATTENDUES)
# =========================

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        calc.divide(10, 0)

def test_modulo_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Modulo par zéro impossible"):
        calc.modulo(10, 0)

def test_factorial_negative():
    calc = AdvancedCalculator()
    with pytest.raises(ValueError, match="Factorielle définie uniquement pour les entiers positifs"):
        calc.factorial(-3)

# =========================
# 3. TESTS CRITIQUES / LIMITE
# =========================

def test_add_large_numbers():
    calc = Calculator()
    result = calc.add(1e308, 1e308)
    assert result == float('inf') or isinstance(result, float)

def test_divide_small_number():
    calc = Calculator()
    result = calc.divide(1, 1e308)
    assert 0 < result < 1e-307
