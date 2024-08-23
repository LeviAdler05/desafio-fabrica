from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)  # Certifique-se de que isso está presente

    def __str__(self):
        return self.titulo

