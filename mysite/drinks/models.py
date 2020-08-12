from django.db import models

# Create your models here.


def get_image_filename(instance, filename):
    id = instance.post.id
    return "food_images/%s" % (id)


class Drinks(models.Model):
    name = models.CharField(max_length=45)
    price = models.PositiveIntegerField(default=None, null=True)
    desc = models.TextField(max_length=1024, null=True, blank=True)
    food_images = models.ImageField(upload_to=get_image_filename,
                                    verbose_name='Image')
    likes = models.PositiveIntegerField(default=0, null=False)

