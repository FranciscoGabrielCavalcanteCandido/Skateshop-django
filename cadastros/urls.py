from django.urls import path
from .views import MarcaCreate, MarcaUpdate
from .views import ProdutoCreate, ProdutoUpdate

urlpatterns = [
    path("cadastrar/marca", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("atualizar/marca/",
         MarcaUpdate.as_view(), name="atualizar-marca"),

    path("cadastrar/produto", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("atualizar/produto/",
         ProdutoUpdate.as_view(), name="atualizar-produto"),
]
