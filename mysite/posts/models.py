from django.db import models
from drinks.models import Drinks
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    likes=models.IntegerField(default=0)
    drink_id = models.ForeignKey(to=Drinks,on_delete=models.CASCADE,related_name="fk_post")
    account = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, related_name="fk_post"
    )