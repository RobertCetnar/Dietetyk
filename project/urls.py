"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dietetyk.views import (landing_page_view,
                            Dashboard,
                            RecipeList,
                            RecipeDetails,
                            AddRecipe,
                            ModifyRecipe,
                            DeleteRecipe,
                            PlanList,
                            PlanDetails,
                            AddPlan,
                            ModifyPlan,
                            DeletePlan,
                            AddPlanRecipe
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landing_page_view),
    path("main/", Dashboard.as_view(), name="main"),
    path("recipe/list/", RecipeList.as_view()),
    path("recipe/<int:id>/", RecipeDetails.as_view()),
    path("recipe/add/", AddRecipe.as_view()),
    path("recipe/modify/<int:id>/", ModifyRecipe.as_view()),
    path("recipe/delete/<int:id>/", DeleteRecipe.as_view()),
    path("plan/list/", PlanList.as_view()),
    path("plan/<int:id>/", PlanDetails.as_view()),
    path("plan/add/", AddPlan.as_view()),
    path("plan/modify/<int:id>/", ModifyPlan.as_view()),
    path("plan/delete/<int:id>/", DeletePlan.as_view()),
    path("plan/add-recipe/", AddPlanRecipe.as_view()),
]
