from this import d
from django.db import models

class shakes(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:15] + '...'