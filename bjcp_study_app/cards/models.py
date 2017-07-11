# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subcategory(models.Model):
	code = models.CharField(max_length=4)
	name = models.CharField(max_length=250)
	impresion_general = models.CharField(max_length=2500)
	aroma = models.CharField(max_length=2500)
	apariencia = models.CharField(max_length=2500)
	sabor = models.CharField(max_length=2500)
	sensacion = models.CharField(max_length=2500)
	ingredientes = models.CharField(max_length=2000)
	comentarios = models.CharField(max_length=2500)
	comparacion = models.CharField(max_length=2500)
	historia = models.CharField(max_length=2500)
	estadisticas = models.CharField(max_length=2500)
	ejemplos = models.CharField(max_length=2050)
	etiquetas = models.CharField(max_length=2500)

	def __str__(self):
		return self.code + " - " + self.name


