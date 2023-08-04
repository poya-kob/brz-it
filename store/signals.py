from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import ProductOutcome


@receiver(pre_delete, sender=ProductOutcome)
def pre_delete_dedications(sender, instance: ProductOutcome, *args, **kwargs):
    instance.product_inventory.inventory += instance.deductions_from_stock
    instance.product_inventory.save()
