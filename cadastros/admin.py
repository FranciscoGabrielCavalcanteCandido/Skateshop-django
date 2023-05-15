from django.contrib import admin
from .models import Marca, Produto, Cliente, Compra, Pagamento

# Register your models here.

admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Pagamento)
