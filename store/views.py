from django.shortcuts import HttpResponse
from .models import Products


def create_product(request):
    pass


def list_products(request, *args, **kwargs):
    pass


def test(request):

    return HttpResponse('test pass')
