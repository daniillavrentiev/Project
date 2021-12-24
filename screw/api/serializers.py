from rest_framework import serializers

from ..models import Product, Products, Categories


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categories
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = '__all__'

    @staticmethod
    def get_products(obj):
        return ProductSerializer(Product.objects.filter(category_id=obj.id), many=True).data


class ProductsProductSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    @staticmethod
    def get_products(obj):
        return ProductsSerializer(Products.objects.filter(product_id=obj), many=True).data
