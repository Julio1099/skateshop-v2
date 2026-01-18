"""
Lógica de controle e exibição (Views) das páginas da loja.
"""

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product


# READ (Listar todos)
class ProductListView(ListView):
    """
    Exibe a lista de todos os produtos disponíveis.
    """

    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"


# READ (Detalhe de um)
class ProductDetailView(DetailView):
    """
    Exibe os detalhes de um único produto.
    """

    model = Product
    template_name = "store/product_detail.html"


# CREATE
class ProductCreateView(CreateView):
    """
    Gerencia o formulário de criação de novos produtos.
    """

    model = Product
    fields = ["name", "category", "price", "stock", "description", "image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("product_list")


# UPDATE
class ProductUpdateView(UpdateView):
    """
    Gerencia a edição de produtos existentes.
    """

    model = Product
    fields = ["name", "category", "price", "stock", "description", "image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("product_list")


# DELETE
class ProductDeleteView(DeleteView):
    """
    Gerencia a exclusão segura de produtos.
    """

    model = Product
    template_name = "store/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")
