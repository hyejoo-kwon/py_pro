from django.db import models

def get_image_filename(instance, filename):
    return "food_images/%s" % filename

def get_brand_name(instance, filename):
    if isinstance(instance, Brand):
        return f"{instance.name}/brand_img"
    return f"{instance.brand.name}/{instance.name}_img"

class Brand(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, unique=True, default="Anoymous")
    desc = models.TextField(max_length=512, null=True, blank=False)
    image = models.ImageField(upload_to=get_brand_name,name="brand_img")
    
class Drinks(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)
    price = models.PositiveIntegerField(default=None, null=True)
    desc = models.TextField(max_length=1024, null=True, blank=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.DO_NOTHING, null=True, default=Brand.objects.first())
    image = models.ImageField(upload_to=get_brand_name, null=True)
    food_images = models.ImageField(upload_to=get_image_filename,
                                    verbose_name='Image')
    likes = models.PositiveIntegerField(default=0, null=False)
    updated_at = models.DateTimeField(auto_now=True)

