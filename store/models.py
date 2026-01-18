"""
Definição dos Modelos de Dados (Tabelas) do sistema de Skate Shop.
"""
from django.db import models


class Category(models.Model):
    """
    Representa as categorias de peças (Shape, Truck, Roda, etc).
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """
    Representa o produto final ou peça à venda na loja.
    """

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    