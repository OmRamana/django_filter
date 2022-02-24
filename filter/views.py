import imp
from django.shortcuts import render
from rest_framework import viewsets
from filter.models import Book
from filter.models import Author
from filter.serializers import BookSerializer,AutherSerializer

class BookViewset(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class AuthorViewset(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AutherSerializer
