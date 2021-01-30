from django.db import models
from datetime import datetime


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    preparation = models.CharField(max_length=256, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(default=datetime.now)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
