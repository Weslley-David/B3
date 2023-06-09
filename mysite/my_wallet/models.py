from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.


class Investidor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    OPERATIONS = (
        ('C', 'Conservador'),
        ('M', 'Moderado'),
        ('A', 'Arrojado'),
    )
    perfil = models.CharField(max_length=1, choices=OPERATIONS)

    def __str__(self) -> str:
        return "{} - {}".format(self.user, self.perfil)


class Stock(models.Model):
    codigo = models.CharField(max_length=6)
    empresa_nome = models.CharField(max_length=100, default='No especified')
    cnpj = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{} - {}".format(self.codigo, self.empresa_nome)


class Transaction(models.Model):
    data = models.DateField("created")
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    quantidade_de_acoes = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    OPERATIONS = (
        ('C', 'Compra'),
        ('V', 'Venda'),
    )
    operacao = models.CharField(max_length=1, choices=OPERATIONS)
    corretagem = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    Investidor = models.ForeignKey(Investidor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - {} - {} - {}".format(self.data, self.stock, self.Investidor.user.username, self.operacao)

    def valor_de_compra(self):
        return self.quantidade_de_acoes * self.preco_unitario

    def taxas_totais(self):
        return self.corretagem + Decimal('1.5')

    def valor_total(self):
        v = self.quantidade_de_acoes * self.preco_unitario
        t = self.corretagem + Decimal('1.5')

        if (self.operacao == "C"):
            print
            return (v + t)
        else:
            return (v - t)
