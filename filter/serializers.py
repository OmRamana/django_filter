from rest_framework import serializers
from filter.models import Book,Author


class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ['author', 'title']


class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'