from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart, Shipment
from cart.serializers import (GetCartSerializer, GetShipmentSerializer,
                              PostCartSerializer, PostShipmentSerializer)


class CartViewSet(viewsets.ModelViewSet):
    """
    list:
        Return a list of all the existing cart.
    create:
        Create a new cart instance.
    retrieve:
        Return the given cart.
    update:
        Update the given cart.
    partial_update:
        Update the given cart given field only.
    destroy:
        Delete the given cart.
    """

    permission_classes = (IsAuthenticated, )
    queryset = Cart.objects.all()
    serializer_class = GetCartSerializer

    def get_serializer_class(self):

        serializer_class = self.serializer_class
        if self.request.method not in ['GET']:
            serializer_class = PostCartSerializer
        return serializer_class


@api_view()
@permission_classes((IsAuthenticated, ))
def get_shipment_status(request):
    """
    Get api to to save third party shipment status.
    """
    import requests
    URL = "http://www.thirdpartyapis.com/api/get_shipment_status/json"
    shipment_id = request.query_params.get('shipment_id')
    PARAMS = {'shipment_id': shipment_id}
    shipment = Shipment.objects.get(id=shipment_id)

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()

    if data['status'] == 'Booked':
        shipment.status='booked'
        shipment.save()
    elif data['status'] == 'In_Print':
        shipment.status='in_print'
        shipment.save()
    elif data['status'] == 'Out_For_shipment':
        shipment.status='out_for_shipment'
        shipment.save()
    else:
        return Response(
            {"Result": "status not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {"Result": "Shipment status saved"},
        status=status.HTTP_200_OK
    )


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    list:
        Return a list of all the existing shipment.
    create:
        Create a new shipment instance.
    retrieve:
        Return the given shipment.
    update:
        Update the given shipment.
    partial_update:
        Update the given shipment given field only.
    destroy:
        Delete the given shipment.
    """

    permission_classes = (IsAuthenticated, )
    queryset = Shipment.objects.all()
    serializer_class = GetShipmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('owner', 'product')

    def get_serializer_class(self):

        serializer_class = self.serializer_class
        if self.request.method not in ['GET']:
            serializer_class = PostShipmentSerializer
        return serializer_class
