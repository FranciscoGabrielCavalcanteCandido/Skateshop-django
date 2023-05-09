from django.urls import path, include
from .views import IndexView, SobreView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("sobre", SobreView.as_view(), name='pagina-sobre'),
    
]
