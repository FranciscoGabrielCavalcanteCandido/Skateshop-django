from django.urls import path
from .views import ClienteCreate, ClienteDelete, ClienteList, ClienteUpdate, MarcaCreate, MarcaUpdate
from .views import ProdutoCreate, ProdutoUpdate
from .views import ProdutoList, MarcaList
from .views import MarcaDelete, ProdutoDelete

urlpatterns = [
    
    # URLS MARCA

    path("cadastrar/marca", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("atualizar/marca/<int:pk>/",
         MarcaUpdate.as_view(), name="atualizar-marca"),
    path("listar/marca", MarcaList.as_view(), name="listar-marca"),
    path("excluir/marca/<int:pk>/", MarcaDelete.as_view(), name="excluir-marca"),

    # URLS MARCA

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
]
