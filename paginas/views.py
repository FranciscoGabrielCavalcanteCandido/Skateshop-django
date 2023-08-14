from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.

class IndexView(TemplateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    template_name = "paginas/modelo.html"


class SobreView(TemplateView, LoginRequiredMixin):
    template_name = "paginas/sobre.html"
