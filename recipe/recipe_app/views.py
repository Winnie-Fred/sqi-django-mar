from django.shortcuts import render, redirect

from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_app/all-recipes.html", {"recipes": recipes})

def add_recipe(request):
    recipe_form = RecipeForm()

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect("recipe_app:all_recipes")

    context = {"recipe_form": recipe_form}
    return render(request, "recipe_app/add-recipe-form.html", context)