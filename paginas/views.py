from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = "paginas/modelo.html"


class SobreView(TemplateView, LoginRequiredMixin):
    template_name = "paginas/sobre.html"
