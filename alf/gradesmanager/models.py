from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    aprovado = models.BooleanField()

class Gabarito(models.Model):
    pergunta = models.TextField()
    resposta = models.TextField()

class Prova(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.PROTECT, blank=True)
    gabarito_id = models.ForeignKey(Gabarito, on_delete=models.PROTECT, blank=True)
    respostas_id = models.ForeignKey('Respostas', on_delete=models.PROTECT, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=1, blank=True)

class Respostas(models.Model):
    prova_id = models.ForeignKey(Prova, on_delete=models.CASCADE)
    pergunta = models.TextField()
    resposta = models.TextField()


