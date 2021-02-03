from random import shuffle

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View

from .models import Recipe, Plan, Dayname, Recipeplan

def landing_page_view(request):
    recipes = list(Recipe.objects.all())
    shuffle(recipes)
    return render(request, "index.html", {"recipes": recipes})


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


class RecipeList(View):
    def get(self, request):
        recipes = Recipe.objects.all().order_by("-votes", "created")
        paginator = Paginator(recipes, 50)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request, "app-recipes.html", {"recipes": recipes, "page_obj": page_obj}
        )


class RecipeDetails(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        return render(
            request,
            "app-recipe-details.html",
            {"recipe": recipe},
        )
    def post(self, request, id):
        id_form = int(request.POST.get("votes"))
        recipe_db = Recipe.objects.get(pk=id)
        if request.POST.get("rating") == "Polub":
            recipe_db.votes += 1
            recipe_db.save()
            return redirect(f"/recipe/{id}/")
        elif request.POST.get("rating") == "Nie lubie":
            recipe_db.votes -= 1
            if recipe_db.votes < 0:
                recipe_db.votes = 0
            recipe_db.save()
            return redirect(f"/recipe/{id}/")


class AddRecipe(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")

    def post(self, request):
        name = request.POST.get("name")
        ingredients = request.POST.get("ingredients")
        description = request.POST.get("description")
        preparation = request.POST.get("preparation")
        preparation_time = int(request.POST.get("prep_time"))
        if not name and not ingredients and not description and not preparation_time:
            return render(
                request, "app-add-recipe.html", {"error": "Fields cannot be empty !!!"}
            )
        else:
            recipe = Recipe()
            recipe.name = name
            recipe.ingredients = ingredients
            recipe.description = description
            recipe.preparation = preparation
            recipe.preparation_time = preparation_time
            recipe.save()
            return redirect("/recipe/list/")


class ModifyRecipe(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        return render(request, "app-edit-recipe.html", {"recipe": recipe})
    def post(self, request, id):
        name = request.POST.get("name")
        ingredients = request.POST.get("ingredients")
        description = request.POST.get("description")
        preparation = request.POST.get("preparation")
        preparation_time = int(request.POST.get("prep_time"))
        if not name and not ingredients and not description and not preparation_time:
            return render(
                request, "app-add-recipe.html", {"error": "Fields cannot be empty !!!"}
            )
        else:
            recipe = Recipe.objects.get(pk=id)
            recipe.name = name
            recipe.ingredients = ingredients
            recipe.description = description
            recipe.preparation = preparation
            recipe.preparation_time = preparation_time
            recipe.save()
            return redirect(f"/recipe/{id}/")


class DeleteRecipe(View):
    def get(self, request, id):
        recipe_to_delete = Recipe.objects.get(pk=id)
        recipe_to_delete.delete()
        return render(request, "dashboard.html")

