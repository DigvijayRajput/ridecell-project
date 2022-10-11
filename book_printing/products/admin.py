from django.contrib import admin

from .models import City, Product, State

admin.site.register(Product)
admin.site.register(City)
admin.site.register(State)
