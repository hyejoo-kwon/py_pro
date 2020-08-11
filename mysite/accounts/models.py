from django.contrib.auth.models import User
from django.db import models
from carts.models import Cart

# Create your models here.

class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cart_id=models.IntegerField()


    @classmethod
    def create(cls):
        cart = Cart.objects.create()
        cart_id=cls(cart_id = cart)

        return cart_id
    
    
