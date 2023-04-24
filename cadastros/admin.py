from django.contrib import admin

# Register your models here.

from .models import Cliente, Marca, Pagamento, Pedido, Produto

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Pagamento)
admin.site.register(Pedido)
admin.site.register(Produto)
