from rest_framework import serializers
from .models import Product, Storage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = "__all__"


class GetStorageSerializer(StorageSerializer):
    products = ProductSerializer(many=True)
