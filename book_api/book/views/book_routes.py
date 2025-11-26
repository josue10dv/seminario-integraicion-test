from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from ..models import Book
from ..serializers import RegisterSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = RegisterSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = (
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
    ordering_fields = ('anio_publicacion', 'titulo', 'autor', 'editorial')
    ordering = ['titulo']  # Orden por defecto

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Libro eliminado exitosamente"},
            status=status.HTTP_204_NO_CONTENT
        )