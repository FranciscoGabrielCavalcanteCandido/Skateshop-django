from cadastros.forms import PedidoForms
from .models import Carrinho, Cliente, Marca, Pedido, Produto, Funcionario, ProdutoPedido
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete

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


class PedidoCreate(LoginRequiredMixin, CreateView):
    form_class = PedidoForms
    template_name = "cadastros/form_pedido.html"
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"titulo": "Cadastro de Pedido"}

    def form_valid(self, form):
        form.instance.valor_total = 0.0

        # cria a venda no banco e o object
        url = super().form_valid(form)

        # faz um select em todos os produtos do carirnho
        produtos_pedido = Carrinho.objects.all()
        valor_total = 0.0

        if (produtos_pedido.count() == 0):
            form.add_error("", "Seu carrinho de compras está vazio!")
            return super().form_invalid(form)

        for i in produtos_pedido:
            valor_total += (float(i.produto.preco) * i.quantidade)

            ProdutoPedido.objects.create(
                produto=i.produto,
                pedido=self.object,
                preco=i.produto.preco * i.quantidade,
                quantidade=i.quantidade
            )

            i.delete()

        self.object.valor_total = valor_total
        self.object.save()

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["carrinho"] = Carrinho.objects.all()

        return context


class CarrinhoCreate(LoginRequiredMixin, CreateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-carrinho")
    extra_context = {"titulo": "Adicionar item ao Carrinho"}


class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = "cadastros/list/pedido.html"
    paginate_by = 50

    # Melhora no desempenho da consulta, isso é um INNER JOIN no atributo CLIENTE
    def get_queryset(self):
        return Pedido.objects.all().select_related("cliente")


class CarrinhoList(LoginRequiredMixin, ListView):
    model = Carrinho
    template_name = "cadastros/list/carrinho.html"
    paginate_by = 50


class ProdutoPedidoList(LoginRequiredMixin, ListView):
    model: ProdutoPedido
    template_name = "cadastros/list/produto_pedido.html"

    def get_queryset(self):
        return ProdutoPedido.objects.filter(pedido__pk=self.kwargs["pk_pedido"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["pedido"] = Pedido.objects.get(pk=self.kwargs["pk_pedido"])

        return context


class CarrinhoUpdate(LoginRequiredMixin, UpdateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-carrinho")


class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-pedido")


class CarrinhoDelete(LoginRequiredMixin, DeleteView):
    model = Carrinho
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-carrinho")


class ClienteAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        object_list = Cliente.objects.all()

        if self.q:
            object_list = object_list.filter(
                nome__icontains=self.q
            )

        return object_list
