from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name="نام")
    inventory = models.IntegerField(verbose_name="موجودی محصول")
    unit = models.CharField(max_length=50, default="عدد")
    created_time = models.DateTimeField(verbose_name="زمان ایجاد محصول", auto_now_add=True)
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ثبت کننده محصول")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")

    # objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام ویژگی')

    def __str__(self):
        return self.name


class AttributeItems(models.Model):
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='items',
                                  verbose_name='ویژگی')
    product: Products = models.ManyToManyField(Products, on_delete=models.PROTECT, related_name='items',
                                               verbose_name='محصول')
    value = models.CharField(max_length=50, verbose_name='مقدار ویژگی')

    def __str__(self):
        return f'{self.product.title} - {self.value}'
