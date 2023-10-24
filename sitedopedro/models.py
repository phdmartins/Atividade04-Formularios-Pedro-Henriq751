from django.db import models

# Create your models here.
class SitesDeReceitas(models.Model):
  nome = models.CharField(max_length=50)
  layout = models.CharField(max_length=70)
  qualidade = models.CharField(max_length=70)
  nota = models.IntegerField()

class MelhoresReceitas(models.Model):
  nome = models.CharField(max_length=50)
  origem = models.CharField(max_length=50)
  nota = models.IntegerField()
  tipo = models.CharField(max_length=50)
  