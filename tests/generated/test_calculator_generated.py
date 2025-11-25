"""
Tests générés automatiquement par IA à partir des spécifications
Fichier source: calculator_spec.txt
"""

import pytest
from src.calculator import Calculator


class TestCalculatorGenerated:
    """Tests générés automatiquement"""

    # Tests pour: addition

    def test_jadditionne(self):
        """
        GIVEN deux nombres positifs
        WHEN j'additionne
        THEN le résultat est la somme
        """
        calculator = Calculator()
        result = calculator.add(5, 3)
        assert result == 8


    def test_jadditionne(self):
        """
        GIVEN un nombre positif et un nombre négatif
        WHEN j'additionne
        THEN le résultat est correct
        """
        calculator = Calculator()
        result = calculator.add(5, -3)
        assert result == 2


    def test_jadditionne(self):
        """
        GIVEN deux nombres décimaux
        WHEN j'additionne
        THEN le résultat est précis
        """
        calculator = Calculator()
        result = calculator.add(5.5, 3.2)
        assert abs(result - 8.7) < 0.01

    # Tests pour: soustraction

    def test_je_soustrais(self):
        """
        GIVEN deux nombres positifs
        WHEN je soustrais
        THEN le résultat est correct
        """
        calculator = Calculator()
        result = calculator.subtract(10, 3)
        assert result == 7


    def test_je_soustrais(self):
        """
        GIVEN le résultat est négatif
        WHEN je soustrais
        THEN le signe est correct
        """
        calculator = Calculator()
        result = calculator.subtract(3, 10)
        assert result == -7

    # Tests pour: multiplication

    def test_je_multiplie(self):
        """
        GIVEN deux nombres positifs
        WHEN je multiplie
        THEN le résultat est le produit
        """
        calculator = Calculator()
        result = calculator.multiply(5, 3)
        assert result == 15


    def test_je_multiplie(self):
        """
        GIVEN un nombre par zéro
        WHEN je multiplie
        THEN le résultat est zéro
        """
        calculator = Calculator()
        result = calculator.multiply(5, 0)
        assert result == 0


    def test_je_multiplie(self):
        """
        GIVEN deux nombres négatifs
        WHEN je multiplie
        THEN le résultat est positif
        """
        calculator = Calculator()
        result = calculator.multiply(-5, -3)
        assert result == 15

    # Tests pour: division

    def test_je_divise(self):
        """
        GIVEN deux nombres où le diviseur n'est pas zéro
        WHEN je divise
        THEN le résultat est correct
        """
        calculator = Calculator()
        result = calculator.divide(10, 2)
        assert result == 5.0


    def test_je_divise(self):
        """
        GIVEN le diviseur est zéro
        WHEN je divise
        THEN une exception ValueError est levée
        """
        calculator = Calculator()
        with pytest.raises(ValueError, match="Division par zéro"):
            calculator.divide(10, 0)


    def test_je_divise(self):
        """
        GIVEN une division décimale
        WHEN je divise
        THEN le résultat est précis
        """
        calculator = Calculator()
        result = calculator.divide(7, 3)
        assert abs(result - 2.333) < 0.01

    # Tests pour: puissance

    def test_je_calcule_la_puissance(self):
        """
        GIVEN une base et un exposant positif
        WHEN je calcule la puissance
        THEN le résultat est correct
        """
        calculator = Calculator()
        result = calculator.power(2, 3)
        assert result == 8


    def test_je_calcule_la_puissance(self):
        """
        GIVEN un exposant négatif
        WHEN je calcule la puissance
        THEN le résultat est un décimal
        """
        calculator = Calculator()
        result = calculator.power(2, -2)
        assert result == 0.25


    def test_je_calcule_la_puissance(self):
        """
        GIVEN un exposant de zéro
        WHEN je calcule la puissance
        THEN le résultat est 1
        """
        calculator = Calculator()
        result = calculator.power(5, 0)
        assert result == 1

    # Tests pour: modulo

    def test_je_calcule_le_modulo(self):
        """
        GIVEN deux nombres positifs
        WHEN je calcule le modulo
        THEN le reste est correct
        """
        calculator = Calculator()
        result = calculator.modulo(10, 3)
        assert result == 1


    def test_je_calcule_le_modulo(self):
        """
        GIVEN le diviseur est zéro
        WHEN je calcule le modulo
        THEN une exception est levée
        """
        calculator = Calculator()
        with pytest.raises(ValueError):
            calculator.modulo(10, 0)

    # Tests pour: factorielle

    def test_je_calcule_la_factorielle(self):
        """
        GIVEN un entier positif
        WHEN je calcule la factorielle
        THEN le résultat est correct
        """
        calculator = Calculator()
        from src.calculator import AdvancedCalculator
        calculator = AdvancedCalculator()
        result = calculator.factorial(5)
        assert result == 120


    def test_je_calcule_la_factorielle(self):
        """
        GIVEN zéro
        WHEN je calcule la factorielle
        THEN le résultat est 1
        """
        calculator = Calculator()
        from src.calculator import AdvancedCalculator
        calculator = AdvancedCalculator()
        result = calculator.factorial(0)
        assert result == 1


    def test_je_calcule_la_factorielle(self):
        """
        GIVEN un nombre négatif
        WHEN je calcule la factorielle
        THEN une exception est levée
        """
        calculator = Calculator()
        from src.calculator import AdvancedCalculator
        calculator = AdvancedCalculator()
        with pytest.raises(ValueError):
            calculator.factorial(-5)

    # Tests pour: nombre premier

    def test_je_vérifie(self):
        """
        GIVEN un nombre premier
        WHEN je vérifie
        THEN retourne True
        """
        calculator = Calculator()
        from src.calculator import AdvancedCalculator
        calculator = AdvancedCalculator()
        assert calculator.is_prime(7) == True


    def test_je_vérifie(self):
        """
        GIVEN un nombre non premier
        WHEN je vérifie
        THEN retourne False
        """
        calculator = Calculator()
        from src.calculator import AdvancedCalculator
        calculator = AdvancedCalculator()
        assert calculator.is_prime(8) == False


    def test_je_vérifie(self):
        """
        GIVEN un nombre inférieur à 2
        WHEN je vérifie
        THEN retourne False
        """
        calculator = Calculator()
        from src.calculator import AdvancedCalculator
        calculator = AdvancedCalculator()
        assert calculator.is_prime(1) == False

