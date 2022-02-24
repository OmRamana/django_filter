from rest_framework import serializers
from filter.models import Book


class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ['author', 'title', 'num_pages']

