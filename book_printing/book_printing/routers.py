from products import views as prod_views
from rest_framework import routers
from cart import views as cart_view

router = routers.DefaultRouter()

router.register('product', prod_views.ProductViewSet)
router.register('cart', cart_view.CartViewSet)
router.register('shipment', cart_view.ShipmentViewSet)
