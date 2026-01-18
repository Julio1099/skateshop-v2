"""
Testes automatizados da aplicação.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Category, Product


class ProductModelTest(TestCase):
    """
    Testes relacionados ao Model de Produtos.
    """

    def setUp(self):
        """
        Configura o cenário antes de cada teste.
        Cria uma categoria fictícia para usar nos produtos.
        """
        self.category = Category.objects.create(name="Shapes", slug="shapes")

    def test_create_product(self):
        """
        Teste: Deve ser possível criar um produto com dados válidos.
        """
        product = Product.objects.create(
            category=self.category,
            name="Shape Maple 8.0",
            description="Madeira de qualidade",
            price=250.00,
            stock=10,
        )

        # Verifica se o produto foi salvo no banco
        self.assertEqual(product.name, "Shape Maple 8.0")
        self.assertEqual(product.price, 250.00)
        self.assertEqual(str(product), "Shape Maple 8.0")

    def test_default_stock(self):
        """
        Teste: Se eu não informar o estoque, ele deve ser 0 (padrão).
        """
        product = Product.objects.create(
            category=self.category,
            name="Rolamento ABEC 5",
            price=80.00,
        )
        self.assertEqual(product.stock, 0)


class ProductViewTest(TestCase):
    """
    Testes relacionados às páginas (Views) e URLs.
    """

    def setUp(self):
        """Cria dados iniciais para exibir nas páginas."""
        self.category = Category.objects.create(name="Roupas", slug="roupas")
        self.product = Product.objects.create(
            category=self.category, name="Camiseta Thrasher", price=120.00, stock=5
        )

    def test_product_list_view_status_code(self):
        """
        Teste: A página inicial (lista de produtos) deve carregar com sucesso (Erro 200).
        """
        url = reverse("product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_list_content(self):
        """
        Teste: A página inicial deve mostrar o produto que criamos.
        """
        url = reverse("product_list")
        response = self.client.get(url)
        # Verifica se o nome do produto aparece no HTML da resposta
        self.assertContains(response, "Camiseta Thrasher")

    def test_create_page_status_code(self):
        """
        Teste: A página de criar produto deve carregar (não pode dar 404).
        """
        url = reverse("product_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
