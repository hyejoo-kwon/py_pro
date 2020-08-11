from django.db import models

# Create your models here.


def get_image_filename(instance, filename):
    id = instance.post.id
    return "food_images/%s" % (id)


class Drinks(models.Model):
    name = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    desc = models.TextField()
    food_images = models.ImageField(upload_to=get_image_filename,
                                    verbose_name='Image')
    likes=models.IntegerField(default=0)
