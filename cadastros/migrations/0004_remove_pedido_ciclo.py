# Generated by Django 4.2.7 on 2023-11-23 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0003_carrinho_funcionario_pedido_produtopedido_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedido",
            name="ciclo",
        ),
    ]