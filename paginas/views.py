from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "paginas/modelo.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
