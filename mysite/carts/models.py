from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Cart(models.Model):
    total_price = models.PositiveIntegerField(default=None, null=True)
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, null=False)



                                                                                                                                                                                                                                    