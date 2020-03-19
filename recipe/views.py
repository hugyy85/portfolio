from django.shortcuts import render, redirect
from recipe.models import User, Recipe
from recipe.forms import CreationFormRecipe
from django.template.context_processors import csrf


def index(request):
    return render(request, 'recipes/index.html', {'recipes': Recipe.objects.all(),
                                                     'users': User.objects.all(),
                                                     })


def get_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = recipe.recipe_ingredients.split('\n')
    instructions = recipe.recipe_steps.split('\n')
    return render(request, 'recipes/get_recipe.html', {'recipe': recipe,
                                                          'ingredients': ingredients,
                                                          'instructions': instructions,
                                                          })


def create_recipe(request):
    args = {'form': CreationFormRecipe}
    args.update(csrf(request))

    if request.method == 'POST':
        form = CreationFormRecipe(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            data = form.data

            new_recipe = Recipe(recipe_name=data['recipe_name'],
                                recipe_description=data['recipe_description'],
                                recipe_ingredients=data['recipe_ingredients'],
                                recipe_steps=data['recipe_steps'],
                                recipe_photo=request.FILES['recipe_photo'],
                                recipe_type_of_meal=data['recipe_type_of_meal'],
                                recipe_author=User.objects.get(user_nickname='Антон')
                                )
            new_recipe.save()

            return redirect('/recipe/')
    else:
        form = CreationFormRecipe()

    return render(request, 'recipes/create_recipe.html', args)