from random import shuffle

from django.shortcuts import render
from django.views import View

from .models import Recipe, Plan, Dayname, Recipeplan


def landing_page_view(request):
    recipes = list(Recipe.objects.all())
    shuffle(recipes)
    return render(request, "index.html", {"recipes": recipes})


def recipe_view(request):
    return render(request, "dashboard.html")


class Dashboard(View):
    def get(self, request):
        days = []
        plans = Plan.objects.all()
        recipe_count = Recipe.objects.all().count()
        plan_count = plans.count()
        last_plan = plans.order_by("-created")[0]
        all_days = Dayname.objects.all()
        for day in all_days:
            recipeplan = Recipeplan.objects.filter(plan=last_plan.id).filter(day_name=day.id).order_by("order")
            if recipeplan:
                days += [
                    {"name": day, "meals": recipeplan}
                ]
        return render(
            request,
            "dashboard.html",
            {"r_count": recipe_count, "p_count": plan_count, "last_plan": last_plan, "days": days},
        )