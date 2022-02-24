import imp
from django.shortcuts import render
from rest_framework import viewsets
from filter.models import Book
from filter.models import Author
from filter.serializers import BookSerializer,AutherSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookViewset(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['author', 'title']


class AuthorViewset(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AutherSerializer
