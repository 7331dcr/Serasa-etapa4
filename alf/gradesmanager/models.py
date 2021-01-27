from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    aprovado = models.BooleanField()

class Gabarito(models.Model):
    gabarito = models.TextField()

class Prova(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    gabarito_id = models.ForeignKey(Gabarito, on_delete=models.PROTECT)
    respostas = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=1)