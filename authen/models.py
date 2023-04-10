from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(max_length=50)
    desc = models.TextField(max_length=100)
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
