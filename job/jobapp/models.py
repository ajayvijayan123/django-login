from django.db import models

# Create your models here.

class table(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)