from django.contrib import admin

from .models import *


class ProductsInlines(admin.TabularInline):

    model = Products


class ProductAdmin(admin.ModelAdmin):

    inlines = [
        ProductsInlines,
    ]


admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)
admin.site.register(Products)



