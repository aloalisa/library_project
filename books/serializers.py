

import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price')














#
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#     subtitle = serializers.CharField()
#


# class CashSerializer(serializers.Serializer):
#     input=serializers.CharField(max_length=150)
#     output=serializers.CharField(max_length=120)
#

