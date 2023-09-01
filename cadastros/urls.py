from django.urls import path
from .views import CarrinhoCreate, CarrinhoDelete, CarrinhoList, CarrinhoUpdate, ClienteAutocomplete, ClienteCreate, ClienteDelete, ClienteList, ClienteUpdate, ProdutoPedidoList
from .views import ProdutoList, MarcaList, MarcaCreate, MarcaUpdate
from .views import ProdutoCreate, ProdutoUpdate
from .views import MarcaDelete, ProdutoDelete
from .views import FuncionarioCreate, FuncionarioUpdate, FuncionárioDelete, FuncionarioList
from .views import PedidoCreate, PedidoList, PedidoDelete


urlpatterns = [
    
    # URLS MARCA

    path("cadastrar/marca", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("atualizar/marca/<int:pk>/",
         MarcaUpdate.as_view(), name="atualizar-marca"),
    path("listar/marca", MarcaList.as_view(), name="listar-marca"),
    path("excluir/marca/<int:pk>/", MarcaDelete.as_view(), name="excluir-marca"),

    # URLS PRODUTO

    path("cadastrar/produto", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("atualizar/produto/<int:pk>/",
         ProdutoUpdate.as_view(), name="atualizar-produto"),
    path("listar/produto", ProdutoList.as_view(), name="listar-produto"),
    path("excluir/produto/<int:pk>/",
         ProdutoDelete.as_view(), name="excluir-produto"),

     # URLS CLIENTE

     path("cadastrar/cliente", ClienteCreate.as_view(), name="cadastrar-cliente"),
     path("atualizar/cliente/<int:pk>/",
          ClienteUpdate.as_view(), name="atualizar-cliente"),
    path("listar/cliente", ClienteList.as_view(), name="listar-cliente"),
    path("excluir/cliente/<int:pk>/",
         ClienteDelete.as_view(), name="excluir-cliente"),

    # URLS FUNCIONARIO

    path("cadastrar/funcionario", FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path("atualizar/funcionario/<int:pk>/",
         FuncionarioUpdate.as_view(), name="atualizar-funcionario"),
    path("listar/cliente", FuncionarioList.as_view(), name="listar-funcionario"),
    path("excluir/cliente/<int:pk>/",
         FuncionárioDelete.as_view(), name="excluir-funcionario"),







    path("cadastrar/pedido", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("listar/pedido", PedidoList.as_view(), name="listar-pedido"),
    path("excluir/pedido/<int:pk>/", PedidoDelete.as_view(), name="excluir-pedido"),
    path("listar/produtos/pedido/<int:pk_pedido>/", ProdutoPedidoList.as_view(),
         name="listar-produtos-pedido"),

    path("cadastrar/carrinho", CarrinhoCreate.as_view(), name="cadastrar-carrinho"),
    path("atualizar/carrinho/<int:pk>/",
         CarrinhoUpdate.as_view(), name="atualizar-carrinho"),
    path("listar/carrinho", CarrinhoList.as_view(), name="listar-carrinho"),
    path("excluir/carrinho/<int:pk>/",
         CarrinhoDelete.as_view(), name="excluir-carrinho"),
    path("buscar/cliente", ClienteAutocomplete.as_view(), name="buscar-cliente")

]
