from django.db import models

class Curso(models.model):
    nome = models.CharField(max_length=200)
    coordenador = models.ForeignKey()
    descricao  =models.TextField(blank=True)
    imagem = models.ImageField(upload_to='assets/administrativo/', blank=True, null=True)


