from django.shortcuts import HttpResponse, render
from django.db.models import Sum

from .models import Products


def create_product(request):
    pass


def list_products(request, *args, **kwargs):
    product_list = Products.objects.all()
    if cat := kwargs.get('cat', False):
        product_list = product_list.filter(category=cat)
    product_list = product_list.annotate(inven=Sum('inv__inventory'))
    context = {
        'products': product_list,
    }

    return render(request, 'product list.html', context)


def detail_product(request, id, name: None):
    product = Products.objects.get(pk=id) or None

    return HttpResponse('detail product')


def test(request):
    return render(request, 'index.html')
