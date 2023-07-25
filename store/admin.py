from django.contrib import admin
from .models import Products, ProductAttribute, AttributeItems, ProductInventory, Category


class AttributeItemsAdmin(admin.StackedInline):
    model = AttributeItems
    extra = 1


class ProductAttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeItemsAdmin]


admin.site.register(Products)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductInventory)
admin.site.register(Category)
