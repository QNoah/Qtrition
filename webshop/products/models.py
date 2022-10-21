from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/templates/images')
    # category = models.ForeignKey('categories', on_delete=models.CASCADE)
