
from rest_framework import serializers
from ..models import Book

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book    
        fields = (
            'id',
            'isbn',
            'titulo',
            'autor',
            'editorial',
            'anio_publicacion',
            'categoria',
            'num_paginas',
            'ubicacion',
            'estado',
            'copias_disponibles'
        )

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book