from rest_framework import filters, viewsets

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    list:
        Return a list of all the existing product.
    create:
        Create a new product instance.
    retrieve:
        Return the given product.
    update:
        Update the given product.
    partial_update:
        Update the given product given field only.
    destroy:
        Delete the given product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
