from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name="نام")
    unit = models.CharField(max_length=50, default="عدد")
    created_time = models.DateTimeField(verbose_name="زمان ایجاد محصول", auto_now_add=True)
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ثبت کننده محصول")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='دسته بندی')
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")

    # objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام ویژگی')

    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی های محصولات'

    def __str__(self):
        return self.name


class AttributeItems(models.Model):
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='items',
                                  verbose_name='ویژگی')
    value = models.CharField(max_length=50, verbose_name='مقدار ویژگی')

    class Meta:
        verbose_name = 'آیتم ویژگی'
        verbose_name_plural = 'آیتم های ویژگی ها'

    def __str__(self):
        return f' {self.value}'


class ProductInventory(models.Model):
    inventory = models.IntegerField(verbose_name="موجودی محصول", default=1)
    income_time = models.DateField(auto_now_add=True, verbose_name='زمان ورود به انبار')
    attribute_item = models.ForeignKey(AttributeItems, on_delete=models.CASCADE,
                                       related_name='inventory', verbose_name='ویژگی مربوطه')
    product: Products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_items',
                                          verbose_name='محصول')

    class Meta:
        verbose_name = 'موجودی محصول'
        verbose_name_plural = 'موجودی محصولات'

    def __str__(self):
        return f'{self.product.title} - {self.attribute_item.value} - {self.inventory}'
