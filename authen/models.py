from django.db import models
from django.core.validators import validate_image_file_extension

# Create your models here.
class Product(models.Model):
    title = models.TextField(max_length=50)
    desc = models.TextField(max_length=100)
    img = models.ImageField(upload_to='images/',validators= [validate_image_file_extension])
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
