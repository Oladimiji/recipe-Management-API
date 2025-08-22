# recipes/serializers.py
from rest_framework import serializers
from .models import Recipe, Category, Ingredient
from django.contrib.auth.models import User

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer for the Ingredient model
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

# Serializer for the Recipe model
class RecipeSerializer(serializers.ModelSerializer):
    # To include the name of the category instead of its ID
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    # To represent ingredients by their names
    ingredients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 
            'title', 
            'description', 
            'instructions', 
            'cooking_time', 
            'preparation_time', 
            'servings', 
            'created_date', 
            'category', 
            'category_name', 
            'ingredients'
        ]
        read_only_fields = ['created_date']
        
        
        # recipes/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Category, Ingredient

# ... (existing serializers)

# Serializer for creating a new user
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user