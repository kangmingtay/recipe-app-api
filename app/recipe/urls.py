from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


# Register viewset with a url router so that endpoint can be accessed from the web
router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]

