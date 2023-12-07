from django.db import models

# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=55)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=55)
    preco = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Preço")
    codigo = models.IntegerField(verbose_name="Código")
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, help_text="Selecione a Marca")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | R${self.preco} | Código: {self.codigo} | Marca: {self.marca.nome}"


class Cliente(models.Model):
    nome = models.CharField(max_length=55)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=10, verbose_name="CEP")
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, verbose_name="Número", null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone} | CEP: {self.cep} | Logradouro: {self.logradouro} | Numero: {self.numero} | Bairro: {self.bairro} | Cidade: {self.cidade}"


class Pagamento(models.Model):
    valor_recebido = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Valor Recebido")
    valor_parcela = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Valor da Parcela")
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    parcelas = models.IntegerField(verbose_name="Parcelas")
    forma_pagamento = models.CharField(
        max_length=55, verbose_name="Forma pagamento")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class Funcionario(models.Model):
    nome = models.CharField(max_length=55)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=55)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone} | Cargo: {self.cargo}"
    

class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, help_text="Selecione um Cliente")
    valor_total = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Preço")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class ProdutoPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    preco = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Preço")
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.produto.nome} ({self.quantidade})'
    

class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Produto: {self.produto} | Qtd. {self.quantidade}'
