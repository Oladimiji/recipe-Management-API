# recipes/models.py
from django.db import models
from django.contrib.auth.models import User

# Define Category first
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name

# Define Ingredient second
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name

# Define Recipe last, since it depends on the others
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    cooking_time = models.PositiveIntegerField(help_text="Cooking time in minutes", null=True, blank=True)
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes", null=True, blank=True)
    servings = models.PositiveIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    # Each recipe is associated with a single creator (User)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # relationships
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def _str_(self):
        return self.title