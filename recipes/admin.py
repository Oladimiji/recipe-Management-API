# recipes/admin.py
from django.contrib import admin
from .models import Recipe, Category, Ingredient

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "cooking_time", "created_date")
    search_fields = ("title", "description", "instructions")
    list_filter = ("category", "created_date")