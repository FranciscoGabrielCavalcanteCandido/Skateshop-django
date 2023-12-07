from typing import Any, Dict
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('login')
    form_class = UsuarioForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registrar novo usuario'

        return context
