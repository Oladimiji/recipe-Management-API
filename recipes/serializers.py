# recipes/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Recipe, Category, Ingredient, Favorite


# -------------------------------
# Category Serializer
# -------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# -------------------------------
# Ingredient Serializer
# -------------------------------
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


# -------------------------------
# Recipe Serializer
# -------------------------------
class RecipeSerializer(serializers.ModelSerializer):
    # Include category name and ingredient names
    category_name = serializers.CharField(source='category.name', read_only=True)
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
            'ingredients',
        ]
        read_only_fields = ['created_date']


# -------------------------------
# User Serializer (for registration)
# -------------------------------
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


# -------------------------------
# Favorite Serializer
# -------------------------------
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'recipe']
        read_only_fields = ['user']


# -------------------------------
# Login Serializer (for custom login)
# -------------------------------
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is deactivated.")

                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                return {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_id": user.id,
                    "username": user.username,
                }
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")