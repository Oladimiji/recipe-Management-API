# recipes/views.py
from rest_framework import viewsets, generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from .models import Recipe, Category, Ingredient, Favorite
from .serializers import (
    RecipeSerializer,
    CategorySerializer,
    IngredientSerializer,
    UserSerializer,
    FavoriteSerializer,
)
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


# ----------------------------
# User Auth Views
# ----------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]


# ----------------------------
# Recipe / Category / Ingredient Views
# ----------------------------
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "ingredients_name", "category_name"]
    filterset_fields = ["category", "cooking_time", "preparation_time", "servings"]
    ordering_fields = ["preparation_time", "cooking_time", "servings", "created_date"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ----------------------------
# Favorite Recipes
# ----------------------------
class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post", "delete"])
    def toggle(self, request, pk=None):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({"detail": "Recipe not found."}, status=status.HTTP_404_NOT_FOUND)

        favorite, created = Favorite.objects.get_or_create
        
        # recipes/views.py
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]