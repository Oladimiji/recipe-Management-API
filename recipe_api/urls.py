from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Make sure you import the FavoriteViewSet
from recipes.views import CategoryViewSet, IngredientViewSet, RecipeViewSet, UserCreateView, FavoriteViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)

# Add this line to register the new viewset
router.register(r'favorites', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Add the user registration URL
    path('api/register/', UserCreateView.as_view(), name='register'),
]