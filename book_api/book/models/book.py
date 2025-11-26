from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=120, unique=True)
    titulo = models.CharField(max_length=500)
    autor = models.CharField(max_length=500)
    editorial = models.CharField(max_length=500)
    anio_publicacion = models.CharField(max_length=500)
    categoria = models.CharField(max_length=500)
    num_paginas = models.IntegerField()
    ubicacion = models.CharField(max_length=500)
    estado = models.CharField(max_length=100)
    copias_disponibles = models.IntegerField()

    class Meta:
        ordering = ("titulo",)
    
    def __str__(self):
        return f'Titulo: {self.titulo}, autor: {self.autor}'
    