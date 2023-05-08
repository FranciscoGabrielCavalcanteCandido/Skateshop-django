from .models import Marca, Produto
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


# CREATE


class MarcaCreate(CreateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


# UPDATE

class MarcaUpdate(UpdateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

# LIST

class MarcaList(ListView):
    model = Marca
    template_name = "cadastros/list/marca.html"


class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/list/produto.html"

# DELETE

class MarcaDelete(DeleteView):
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/list/delete.html"
    success_url = reverse_lazy("listar-produto")
