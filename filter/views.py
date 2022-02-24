from django.shortcuts import render
from rest_framework import viewsets
from filter.models import Book
from filter.serializers import BookSerializer

class BookViewset(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer