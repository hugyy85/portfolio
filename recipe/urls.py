from django.urls import path, include
from recipe import views


urlpatterns = [
    path('', views.index, name='recipe'),
    path('create/', views.create_recipe, name='create-recipe'),
    path('get/<int:recipe_id>/', views.get_recipe, name='get-recipe'),

]