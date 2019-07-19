from django.forms import ModelForm
from recipe.models import User, Recipe


class CreationFormRecipe(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['recipe_status', 'recipe_likes', 'recipe_created', 'recipe_update', 'recipe_author']
