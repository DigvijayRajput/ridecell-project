from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """
    This model will keep all product details
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        """
        Str magic method is override to return string
        representation of an objects.
        """
        return self.title


class City(models.Model):
    """
    This model will keep all city related data
    """
    name = models.CharField(max_length=150)


class State(models.Model):
    """
    This model will keep all state related data
    """
    name = models.CharField(max_length=150)


class UserProfile(models.Model):
    """
    This model will keep all user profile details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    zip_code = models.CharField(max_length=15, null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
