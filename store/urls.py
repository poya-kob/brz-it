from django.urls import path

from .views import list_products, detail_product, income_product

urlpatterns = [
    path('product/income', income_product, name='income-product'),
    path('product/', list_products, name='list-product'),
    path('product/<int:id>', detail_product),
    path('product/<int:id>/<str:name>/', detail_product),
]
