from rest_framework import viewsets

from .serializers import *
from ..models import *


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductsCategoryViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = ProductCategorySerializer

    action_to_serializer = {
        "retrieve": ProductCategorySerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class ProductsProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductsProductSerializer

    action_to_serializer = {
        "retrieve": ProductsProductSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )