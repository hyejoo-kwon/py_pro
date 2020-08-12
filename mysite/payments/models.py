from django.db import models

# models
from carts.models import Cart


class Payment(models.Model):
    is_paid = models.BooleanField(default=False, null=False)
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, to_field='payments')
    total_price = models.
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(verbose_name="paid date",null=True,default=null) 

