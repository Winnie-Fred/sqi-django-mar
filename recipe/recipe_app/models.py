from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the recipe")
    ingredients = models.TextField(help_text="Comma-separated ingredients for the recipe")
    instructions = models.TextField(help_text="Cooking instructions for the recipe")
    cooking_time = models.PositiveIntegerField(help_text="Time in minutes")
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)
    

    
