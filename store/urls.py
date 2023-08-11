from django.urls import path

from .views import test, list_products, detail_product

urlpatterns = [
    path('', test),
    path('product/', list_products, name='list-product'),
    path('product/<int:id>', detail_product),
    path('product/<int:id>/<str:name>/', detail_product),
]
