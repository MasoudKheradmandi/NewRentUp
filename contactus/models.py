from django.db import models

# Create your models here.
class Khabarname(models.Model):
    email = models.EmailField(max_length=254,unique=True)

    class Meta:
        verbose_name = "خبرنامه"
        verbose_name_plural =  "خبرنامه"

    def __str__(self):
        return self.email