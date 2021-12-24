from django.urls import path

from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('products_category', ProductsCategoryViewSet, basename='products_category')
router.register('products_product', ProductsProductViewSet, basename='products_product')


urlpatterns = []
urlpatterns += router.urls