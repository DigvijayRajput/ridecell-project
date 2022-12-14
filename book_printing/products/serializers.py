from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Product model sereailzer.
    """

    class Meta:
        model = Product
        fields = '__all__'
