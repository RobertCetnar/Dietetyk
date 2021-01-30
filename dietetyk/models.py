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


class Plan(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    created = models.DateField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe, through="Recipeplan")


class Dayname(models.Model):
    name = models.CharField(max_length=64)
    order = models.IntegerField(unique=True)


class Recipeplan(models.Model):
    meal_name = models.CharField(max_length=64)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    day_name = models.ForeignKey(Dayname, on_delete=models.CASCADE)