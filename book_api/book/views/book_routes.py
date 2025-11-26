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
        
    def calculate_avarage(self, request, *args, **kwargs):
        numeros = request.data.get('numeros', [])
        if len(numeros) == 0:
            return Response(
                {"error": "La lista de números no puede estar vacía."},
                status=status.HTTP_400_BAD_REQUEST
            )
        total_prestamos = 0
        for num in numeros:
            total_prestamos += num
        promedio = total_prestamos / len(numeros)
        return Response({"promedio": promedio}, status=status.HTTP_200_OK)
    
    def calculate_fine(self, request, *args, **kwargs):
        dias_atraso = request.data.get('dias_atraso', 0)
        multa_por_dia = request.data.get('multa_por_dia', 0)
        msg = ""
        if dias_atraso <= 0:
            msg = "No hay multa, el libro fue devuelta a tiempo."
        else:
            multa = dias_atraso * multa_por_dia
            msg = f"La multa es de ${multa} por {dias_atraso} días de atraso."
        return Response({"mensaje": msg}, status=status.HTTP_200_OK)
        