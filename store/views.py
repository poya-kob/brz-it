from django.shortcuts import HttpResponse
from django.db.models import Sum

from .models import Products


def create_product(request):
    pass


def list_products(request, *args, **kwargs):
    product_list = Products.objects.all()
    if cat := kwargs.get('cat', False):
        product_list = product_list.filter(category=cat)
    product_list = product_list.annotate(inven=Sum('inv__inventory'))

    return HttpResponse('list products')


def detail_product(request, id, name: None):
    product = Products.objects.get(pk=id) or None

    return HttpResponse('detail product')


def test(request):
    return HttpResponse('test pass')
