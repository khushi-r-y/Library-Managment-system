from rest_framework import serializers
from .models import Category,Book,BookCopy
class CategorySerializer(serializers.ModelSerializer):
    class Meta: model=Category; fields='__all__'
class BookSerializer(serializers.ModelSerializer):
    class Meta: model=Book; fields='__all__'
class BookCopySerializer(serializers.ModelSerializer):
    class Meta: model=BookCopy; fields='__all__'
