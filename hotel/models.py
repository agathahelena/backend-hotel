from django.db import models

class Reserva(models.Model):
    dataEntra = models.DateField()
    dataSai =  models.DateField()
    PessoasQuantidade = models.CharField(max_length=5)

    def __str__(self):
        return self.PessoasQuantidade 

class Funcionario(models.Model):
    dataRegistro = models.DateField()
    CPF = models.CharField(max_length=11)
    cod = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=15) 

    def __str__(self): 
        return self.nome

class Servico(models.Model):
    codServico = models.CharField(max_length=10)
    horaServico = models.TimeField(max_length=5)
    QuartoServico = models.CharField(max_length=3)

    def __str__(self):
        return self.codServico

