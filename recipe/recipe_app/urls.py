from django.urls import path

from . import views 

app_name = "recipe_app"

urlpatterns = [
    path("all-recipes/", views.all_recipes, name="all_recipes"),
    path("add-recipe/", views.add_recipe, name="add_recipe"),
]