from django.db import models

# Create your models here.
class commentHome(models.Model):
    name = models.CharField(max_length=100)
    alt = models.CharField(max_length=50)
    image = models.ImageField()
    text = models.TextField()

