from django.db import models

# models
from carts.models import Cart
from drinks.models import Drinks


class Payment(models.Model):
    is_paid = models.BooleanField(default=False, null=False)
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name="payments")
    total_price = models.PositiveIntegerField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="paid date",null=True,default=None) 


class PaymentRow(models.Model):
    drink = models.ForeignKey(to=Drinks, on_delete=models.CASCADE, related_name="payments")
    quantity = models.PositiveIntegerField(default=None, null=True)
    payment = models.ForeignKey(to=Payment, on_delete=models.CASCADE, related_name='items')

