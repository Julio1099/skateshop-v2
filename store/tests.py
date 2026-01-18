"""
Testes automatizados da aplicação.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    """
    Classe de testes básicos para garantir que o ambiente está rodando.
    """

    def test_ambiente(self):
        """Testa se 1 + 1 é igual a 2 (Smoke Test)."""
        self.assertEqual(1 + 1, 2)
