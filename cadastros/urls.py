from django.urls import path
from .views import MarcaCreate, MarcaUpdate
from .views import ProdutoCreate, ProdutoUpdate
from .views import ProdutoList, MarcaList
from .views import MarcaDelete, ProdutoDelete

urlpatterns = [
    path("cadastrar/marca", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("atualizar/marca/",
         MarcaUpdate.as_view(), name="atualizar-marca"),
    path("listar/marca", MarcaList.as_view(), name="listar-marca"),
    path("excluir/marca/<int:pk>/", MarcaDelete.as_view(), name="excluir-marca"),

    path("cadastrar/produto", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("atualizar/produto/",
         ProdutoUpdate.as_view(), name="atualizar-produto"),
    path("listar/produto", ProdutoList.as_view(), name="listar-produto"),
    path("excluir/produto/<int:pk>/",
         ProdutoDelete.as_view(), name="excluir-produto"),
]
