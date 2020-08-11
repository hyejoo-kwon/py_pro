from django.db import models

# Create your models here.

class Cart(models.Model):
    sum=models.CharField(max_length=50, null=True, blank=False, default='0')



                                                                                                                                                                                                                                    