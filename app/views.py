from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product, Storage
from .serializers import ProductSerializer, StorageSerializer, GetStorageSerializer


class ProductListView(ListAPIView):
    """Получение товаров"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('code', 'group', 'storage')
    filter_backends = [DjangoFilterBackend]


class StorageListView(ListAPIView):
    """Получение складов"""
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageRetrieveAPIView(RetrieveAPIView):
    """Получение склада и его товаров"""
    queryset = Storage.objects.all()
    serializer_class = GetStorageSerializer
