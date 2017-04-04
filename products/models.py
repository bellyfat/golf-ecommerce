from __future__ import unicode_literals

from django.db import models

# Here I have created my models

class Product(models.Model):
    name=models.CharField(max_length=255, default='')
    description = models.TextField()
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
