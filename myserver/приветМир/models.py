from django.db import models


# Create your models here.
class TestCat(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    prise = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=TestCat, on_delete=models.CASCADE)
