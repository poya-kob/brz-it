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
    unit = models.CharField(max_length=50, default="عدد")
    income_time = models.DateField(auto_now_add=True, verbose_name='زمان ورود به انبار')
    product: Products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='inv',
                                          verbose_name='محصول')
    attribute_item = models.ForeignKey(AttributeItems, on_delete=models.CASCADE,
                                       related_name='inventory', verbose_name='ویژگی مربوطه')

    class Meta:
        verbose_name = 'موجودی محصول'
        verbose_name_plural = 'موجودی محصولات'

    def __str__(self):
        return f'{self.product.title} - {self.attribute_item.value} - {self.inventory}'


class ProductOutcome(models.Model):
    _original_deductions = 0
    deductions_from_stock = models.IntegerField(verbose_name='تعداد کسر از انبار')
    outcome_time = models.DateField(auto_now_add=True, verbose_name="زمان خروج از انبار")
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.PROTECT, related_name='outcome',
                                          verbose_name='موجودی')
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'کسری محصول'
        verbose_name_plural = 'کسری محصولات'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.deductions_from_stock:
            self._original_deductions = self.deductions_from_stock

    def __str__(self):
        return f'{self.product_inventory.product.title} - {self.product_inventory.attribute_item.value} - {self.deductions_from_stock}'

    def save(self, *args, **kwargs):
        if self._original_deductions != self.deductions_from_stock:
            self.product_inventory.inventory += self._original_deductions
            self.product_inventory.inventory -= self.deductions_from_stock
            self.product_inventory.save()
        return super().save(*args, **kwargs)
