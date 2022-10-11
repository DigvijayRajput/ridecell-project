from rest_framework import serializers

from .models import Cart, Shipment


class GetCartSerializer(serializers.ModelSerializer):
    """
    Cart model sereailzer.
    """

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1


class PostCartSerializer(serializers.ModelSerializer):
    """
    Cart model sereailzer.
    """

    class Meta:
        model = Cart
        fields = '__all__'


class GetShipmentSerializer(serializers.ModelSerializer):
    """
    GetSheepment model sereailzer.
    """

    class Meta:
        model = Shipment
        fields = '__all__'
        depth = 1


class PostShipmentSerializer(serializers.ModelSerializer):
    """
    PostSheepment model sereailzer.
    """

    class Meta:
        model = Shipment
        fields = '__all__'
