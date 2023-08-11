from django.shortcuts import HttpResponse, render
from django.db.models import Sum

from .models import Products, Category


def create_product(request):
    pass


def list_products(request):
    product_list = Products.objects.all()
    if cat := request.GET.get('cat', False):
        product_list = product_list.filter(category__name=cat)
    product_list = product_list.annotate(inven=Sum('inv__inventory'))

    categories = Category.objects.all()
    context = {
        'products': product_list,
        'categories': categories,

    }

    return render(request, 'product_list.html', context)


def detail_product(request, id, name=None):
    product = Products.objects.get(pk=id) or None

    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


def test(request):
    return render(request, 'index.html')
