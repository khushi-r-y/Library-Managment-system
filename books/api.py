from rest_framework import viewsets
from .models import Category,Book,BookCopy
from .serializers import CategorySerializer,BookSerializer,BookCopySerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all(); serializer_class=CategorySerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.select_related('category').all(); serializer_class=BookSerializer
class BookCopyViewSet(viewsets.ModelViewSet):
    queryset=BookCopy.objects.select_related('book').all(); serializer_class=BookCopySerializer
