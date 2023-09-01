from dal import autocomplete
from django import forms
from .models import Pedido


class PedidoForms(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "valor_total"]
        widgets = {
            'cliente': autocomplete.ModelSelect2(
                url='buscar-cliente'
            )
        }
