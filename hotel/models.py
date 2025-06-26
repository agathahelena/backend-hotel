from django.db import models

class Hospede(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=19)
    dataNascimento = models.DateField(max_length=10)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    numero = models.CharField(max_length=4)
    quantidadePessoas = models.CharField(max_length=1)

    def __str__(self):
        return self.numero

class Pagamento(models.Model):
    valor = models.CharField(max_length=5)
    formaPagamento = models.CharField(max_length=15)
    data = models.DateField(max_length=10)
    hora = models.TimeField(max_length=3)

    def __str__(self):
        return self.valor

class FuncaoFuncionario(models.Model):
    nome = models.CharField(max_length=15)
    funcionario = models.CharField(max_length=30)

    def __str__(self):
        return self.nome