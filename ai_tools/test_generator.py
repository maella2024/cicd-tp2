"""
Générateur automatique de tests à partir de spécifications textuelles
Simule l'utilisation d'un LLM pour transformer du langage naturel en code de test
"""

import re
from typing import List, Dict
from pathlib import Path


class TestGenerator:
    """Génère des tests pytest à partir de spécifications Given-When-Then"""

    def __init__(self, specs_file: str):
        self.specs_file = Path(specs_file)
        self.specs = self._parse_specifications()

    def _parse_specifications(self) -> Dict[str, List[str]]:
        """Parse le fichier de spécifications et extrait les scénarios"""
        with open(self.specs_file, 'r', encoding='utf-8') as f:
            content = f.read()

        specs = {}
        current_section = None

        # Extraction des sections et scénarios
        for line in content.split('\n'):
            # Détection des sections (### Titre)
            if line.startswith('###'):
                current_section = line.replace('#', '').strip().lower()
                specs[current_section] = []
            # Détection des scénarios (- GIVEN...)
            elif line.startswith('- GIVEN') and current_section:
                specs[current_section].append(line[2:])  # Retire "- "

        return specs

    def _generate_test_name(self, scenario: str) -> str:
        """Génère un nom de test à partir d'un scénario"""
        # Extraire les parties clés du scénario
        match = re.search(r'WHEN (.+?) THEN', scenario)
        if match:
            action = match.group(1).strip()
            # Nettoyer et convertir en snake_case
            test_name = re.sub(r'[^\w\s]', '', action)
            test_name = test_name.lower().replace(' ', '_')
            return f"test_{test_name}"
        return "test_scenario"

    def _generate_test_body(self, section: str, scenario: str) -> str:
        """Génère le corps du test en fonction du scénario"""
        # Parser le scénario
        given_match = re.search(r'GIVEN (.+?) WHEN', scenario)
        when_match = re.search(r'WHEN (.+?) THEN', scenario)
        then_match = re.search(r'THEN (.+?)$', scenario)

        given = given_match.group(1) if given_match else ""
        when = when_match.group(1) if when_match else ""
        then = then_match.group(1) if then_match else ""

        # Génération du code selon la section
        code = self._map_scenario_to_code(section, given, when, then)

        return f'''        """
        GIVEN {given}
        WHEN {when}
        THEN {then}
        """
        calculator = Calculator()
{code}'''

    def _map_scenario_to_code(self, section: str, given: str, when: str, then: str) -> str:
        """Mappe un scénario vers du code Python concret (logique simplifiée)"""

        # Mapping basé sur les mots-clés
        if section == "addition":
            if "positifs" in given:
                return "        result = calculator.add(5, 3)\n        assert result == 8"
            elif "négatif" in given:
                return "        result = calculator.add(5, -3)\n        assert result == 2"
            elif "décimaux" in given:
                return "        result = calculator.add(5.5, 3.2)\n        assert abs(result - 8.7) < 0.01"

        elif section == "soustraction":
            if "positifs" in given:
                return "        result = calculator.subtract(10, 3)\n        assert result == 7"
            elif "négatif" in given:
                return "        result = calculator.subtract(3, 10)\n        assert result == -7"

        elif section == "multiplication":
            if "positifs" in given:
                return "        result = calculator.multiply(5, 3)\n        assert result == 15"
            elif "zéro" in given:
                return "        result = calculator.multiply(5, 0)\n        assert result == 0"
            elif "négatifs" in given:
                return "        result = calculator.multiply(-5, -3)\n        assert result == 15"

        elif section == "division":
            if "n'est pas zéro" in given:
                return "        result = calculator.divide(10, 2)\n        assert result == 5.0"
            elif "zéro" in given:
                return "        with pytest.raises(ValueError, match=\"Division par zéro\"):\n            calculator.divide(10, 0)"
            elif "décimale" in given:
                return "        result = calculator.divide(7, 3)\n        assert abs(result - 2.333) < 0.01"

        elif section == "puissance":
            if "positif" in given:
                return "        result = calculator.power(2, 3)\n        assert result == 8"
            elif "négatif" in given:
                return "        result = calculator.power(2, -2)\n        assert result == 0.25"
            elif "zéro" in given:
                return "        result = calculator.power(5, 0)\n        assert result == 1"

        elif section == "modulo":
            if "positifs" in given:
                return "        result = calculator.modulo(10, 3)\n        assert result == 1"
            elif "zéro" in given:
                return "        with pytest.raises(ValueError):\n            calculator.modulo(10, 0)"

        elif section == "factorielle":
            if "positif" in given and "zéro" not in given:
                return "        from src.calculator import AdvancedCalculator\n        calculator = AdvancedCalculator()\n        result = calculator.factorial(5)\n        assert result == 120"
            elif "zéro" in given:
                return "        from src.calculator import AdvancedCalculator\n        calculator = AdvancedCalculator()\n        result = calculator.factorial(0)\n        assert result == 1"
            elif "négatif" in given:
                return "        from src.calculator import AdvancedCalculator\n        calculator = AdvancedCalculator()\n        with pytest.raises(ValueError):\n            calculator.factorial(-5)"

        elif section == "nombre premier":
            if "premier" in given and "non" not in given:
                return "        from src.calculator import AdvancedCalculator\n        calculator = AdvancedCalculator()\n        assert calculator.is_prime(7) == True"
            elif "non premier" in given:
                return "        from src.calculator import AdvancedCalculator\n        calculator = AdvancedCalculator()\n        assert calculator.is_prime(8) == False"
            elif "inférieur" in given:
                return "        from src.calculator import AdvancedCalculator\n        calculator = AdvancedCalculator()\n        assert calculator.is_prime(1) == False"

        # Par défaut
        return "        # TODO: Implémenter ce test\n        pass"

    def generate_tests(self, output_file: str):
        """Génère le fichier de tests complet"""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # En-tête du fichier
        content = '''"""
Tests générés automatiquement par IA à partir des spécifications
Fichier source: {}
"""

import pytest
from src.calculator import Calculator


class TestCalculatorGenerated:
    """Tests générés automatiquement"""

'''.format(self.specs_file.name)

        # Génération des tests
        for section, scenarios in self.specs.items():
            content += f"    # Tests pour: {section}\n"
            for scenario in scenarios:
                test_name = self._generate_test_name(scenario)
                test_body = self._generate_test_body(section, scenario)
                content += f"\n    def {test_name}(self):\n{test_body}\n\n"

        # Écriture du fichier
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Tests générés avec succès: {output_path}")
        print(f"📊 Nombre de sections: {len(self.specs)}")
        print(f"📊 Nombre total de tests: {sum(len(scenarios) for scenarios in self.specs.values())}")


def main():
    """Point d'entrée principal"""
    generator = TestGenerator('specs/calculator_spec.txt')
    generator.generate_tests('tests/generated/test_calculator_generated.py')


if __name__ == '__main__':
    main()