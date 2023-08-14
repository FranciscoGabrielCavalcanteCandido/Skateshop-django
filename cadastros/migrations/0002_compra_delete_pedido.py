# Generated by Django 4.1.5 on 2023-05-23 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_compra", models.IntegerField(verbose_name="ID Compra")),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                (
                    "produtos",
                    models.ForeignKey(
                        help_text="Selecione um Produto",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.produto",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Pedido",
        ),
    ]