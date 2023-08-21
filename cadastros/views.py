from .models import Cliente, Marca, Produto, Funcionario
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


# CREATE


class MarcaCreate(CreateView, LoginRequiredMixin):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Cadastro de Marca"}


class ProdutoCreate(CreateView, LoginRequiredMixin):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}


class ClienteCreate(CreateView, LoginRequiredMixin):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Cadastro de Cliente"}


class FuncionarioCreate(CreateView, LoginRequiredMixin):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "cargo"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Cadastro de Funcionário"}


# UPDATE

class MarcaUpdate(UpdateView, LoginRequiredMixin):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Atualizar Marca"}


class ProdutoUpdate(UpdateView, LoginRequiredMixin):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Atualizar Produto"}


class ClienteUpdate(UpdateView, LoginRequiredMixin):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Atualizar Cliente"}


class FuncionarioUpdate(UpdateView, LoginRequiredMixin):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "cargo"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Atualizar Funcionário"}


# LIST

class MarcaList(ListView, LoginRequiredMixin):
    model = Marca
    template_name = "cadastros/list/marca.html"
    paginate_by = 10


class ProdutoList(ListView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/list/produto.html"
    paginate_by = 10


class ClienteList(ListView, LoginRequiredMixin):
    model = Cliente
    template_name = "cadastros/list/cliente.html"
    paginate_by = 10


class FuncionarioList(ListView, LoginRequiredMixin):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"
    paginate_by = 10


# DELETE

class MarcaDelete(DeleteView, LoginRequiredMixin):
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoDelete(DeleteView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")


class ClienteDelete(DeleteView, LoginRequiredMixin):
    model = Cliente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-cliente")


class FuncionárioDelete(DeleteView, LoginRequiredMixin):
    model = Funcionario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-funcionario")
