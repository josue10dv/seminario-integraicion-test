from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo', 'autor', 'editorial', 'anio_publicacion', 'estado', 'copias_disponibles')
    list_filter = ('estado', 'categoria', 'editorial')
    search_fields = ('isbn', 'titulo', 'autor', 'editorial')
    ordering = ('titulo',)
