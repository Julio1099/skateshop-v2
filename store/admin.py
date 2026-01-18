"""
Configuração da interface administrativa do Django.
"""

from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configura a listagem de produtos no Admin, adicionando filtros e colunas.
    """

    list_display = ["name", "price", "stock", "category"]
    list_filter = ["category"]


admin.site.register(Category)
