from django.contrib import admin
from recipe.models import User, Recipe


class UserAdmin(admin.ModelAdmin):
    exclude = ['user_status']
    #list_filter = ['number']
    # search_fields = ['who_call', ]


class RecipeAdmin(admin.ModelAdmin):
    exclude = ['recipe_status', 'recipe_likes']
    # list_filter = ['numbers']
    # search_fields = ['name', ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(User, UserAdmin)