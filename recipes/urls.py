from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    RecipeViewSet,
    CategoryViewSet,
    IngredientViewSet,
    FavoriteViewSet,
    RegisterView,
)

# Router for ViewSets
router = DefaultRouter()
router.register(r"recipes", RecipeViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"ingredients", IngredientViewSet)
router.register(r"favorites", FavoriteViewSet, basename="favorite")

# Combine everything into one urlpatterns
urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
]