from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
