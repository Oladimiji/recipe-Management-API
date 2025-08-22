# recipes/views.py
from rest_framework import viewsets, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend  # <-- Add this import
# ... other imports
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, permissions, filters
from .models import Recipe, Category, Ingredient
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsAuthorOrReadOnly

# Viewset for the Recipe model.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Add these lines to enable searching and ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'ingredients__name'] # You'll need to update this with your field names
    ordering_fields = ['preparation_time', 'cooking_time', 'servings']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# View for user registration
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category_name', 'ingredients_name']
    ordering_fields = ['preparation_time', 'cooking_time', 'servings']

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the recipe
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    # recipes/views.py
from rest_framework import viewsets
from .models import Recipe, Category, Ingredient
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer

# Viewset for the Category model
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Viewset for the Ingredient model
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

# Viewset for the Recipe model
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    
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
    
    # recipes/views.py

# ... (other viewsets and code)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Add the filtering and searching backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Configure the fields that can be searched
    search_fields = ['title', 'ingredients_name', 'category_name']
    
    # Configure the fields that can be filtered
    filterset_fields = ['category', 'cooking_time', 'preparation_time', 'servings']
    
    # Configure the fields that can be used for sorting
    ordering_fields = ['preparation_time', 'cooking_time', 'servings', 'created_date']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)