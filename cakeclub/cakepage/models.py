from django.db import models
import datetime
from django.utils import timezone
from multiselectfield import MultiSelectField

# Create your models here.

class DuplaDaVez(models.Model):
    nome_um = models.CharField(max_length=50)
    nome_dois = models.CharField(max_length=50)
    date_da_dupla = models.DateField('Data da dupla')

#possivel retorno da classe    
    def __str__(self):
        return '%s %s %s %s' % (self.id, self.nome_um, self.nome_dois, self.date_da_dupla)

class Cakes(models.Model):
    """Model definition for Cakes."""

    name = models.CharField(verbose_name='Nome', max_length=50)

    class Meta:
        """Meta definition for Cakes."""

        verbose_name = 'Cakes'
        verbose_name_plural = 'Cakess'

    def __str__(self):
        return self.name
           

class CakePool(models.Model):
    """Model definition for Pool."""
    entry_date = models.DateTimeField(verbose_name='Data da resposta', auto_now=False, auto_now_add=True)
    cake = models.ManyToManyField(Cakes, related_name='cake_pool')

    class Meta:
        """Meta definition for Pool."""

        verbose_name = 'Pool'
        verbose_name_plural = 'Pools'
        

    def __str__(self):
        return '%s %s' % (self.entry_date, self.cake.all()) #cake.all para regularização dos nomes dentro das escolhas



class Dicas(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=300)
    
    class Meta:
        verbose_name = 'titulo'
        verbose_name_plural = 'titulos'

    def __unicode__(self):
        return self.titulo
        