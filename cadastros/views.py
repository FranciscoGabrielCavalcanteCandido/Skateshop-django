from .models import Cliente, Marca, Produto, Funcionario
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


# CREATE


class MarcaCreate(CreateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Cadastro de Marca"}


class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}


class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Cadastro de Cliente"}


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "cargo"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Cadastro de Funcionário"}


# UPDATE

class MarcaUpdate(UpdateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Atualizar Marca"}


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Atualizar Produto"}


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Atualizar Cliente"}


class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "cargo"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Atualizar Funcionário"}


# LIST

class MarcaList(ListView):
    model = Marca
    template_name = "cadastros/list/marca.html"
    paginate_by = 10


class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/list/produto.html"
    paginate_by = 10


class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"
    paginate_by = 10


class FuncionarioList(ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"
    paginate_by = 10


# DELETE

class MarcaDelete(DeleteView):
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-cliente")


class FuncionárioDelete(DeleteView):
    model = Funcionario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-funcionario")
