from django.contrib.auth.models import User
from django.db import models
from products.models import Product, UserProfile


class Type(models.Model):
    """
    This model will keep types details
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    This model will keep all cart details.
    """
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=100, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    book_type = models.ManyToManyField(Type)


class Shipment(models.Model):
    """
    This model will keep all sheepment detail.
    """
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ShipmentTracker(models.Model):
    """
    This model will keep all sheepment detail.
    """
    STATUS_CHOICES = (
        ('booked', 'Booked'), 
        ('in_print', 'In_Print'), 
        ('out_for_shipment', 'Out_For_shipment')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
