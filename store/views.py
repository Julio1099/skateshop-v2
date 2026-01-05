from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

# READ (Listar todos)
class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

# READ (Detalhe de um)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

# CREATE
class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'price', 'stock', 'description', 'image']
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

# UPDATE
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'price', 'stock', 'description', 'image']
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

# DELETE
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')