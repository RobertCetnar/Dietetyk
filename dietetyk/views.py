from random import shuffle

from django.shortcuts import render
from .models import Recipe


def landing_page_view(request):
    recipes = list(Recipe.objects.all())
    shuffle(recipes)
    return render(request, "index.html", {"recipes": recipes})
