from django.db import models
import datetime


class Registro_de_chamados(models.Model):

    id_chamado = models.AutoField(primary_key=True)
    numero_salt = models.CharField(max_length=100)
    data_envio = models.CharField(max_length=100, default = datetime.date.today().isoformat())
    time = models.CharField(max_length=100)
    hashtags = models.CharField(max_length=20, blank=True)
    situacoes = models.CharField(max_length=50)
    colaborador = models.CharField(max_length=50)

    def __str__(self):
        return self.numero_salt
