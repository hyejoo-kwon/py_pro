from django.db import models
from drinks.models import Drinks
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    likes=models.IntegerField(default=0, null=False)
    drink = models.ForeignKey(to=Drinks,on_delete=models.CASCADE,related_name="post")
    account = models.ForeignKey(
        to=get_user_model(), on_delete=models.DO_NOTHING, related_name="fk_post"
    )
    content = models.TextField(blank=True, null=False, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 