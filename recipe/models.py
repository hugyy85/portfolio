from django.db import models


class User(models.Model):
    user_nickname = models.CharField(max_length=64)
    user_email = models.EmailField()
    user_status = models.BooleanField(default=True)
    user_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # user_favourite = models.ForeignKey(Recipe)

    def __str__(self):
        return f'{self.user_nickname}'

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=64)
    recipe_description = models.CharField(max_length=1024)
    recipe_ingredients = models.TextField(default='Вводите через запятую')
    recipe_steps = models.TextField()
    recipe_photo = models.ImageField(upload_to='media/upload/')
    TYPE_OF_MEAL_CHOICE = [
        ('salad', 'Салат'),
        ('soup', 'Суп'),
        ('first', 'Первое'),
        ('second', 'Второе'),
        ('dessert', 'Десерт'),
        ('drinks', 'Напиток'),
    ]
    recipe_type_of_meal = models.CharField(max_length=128, choices=TYPE_OF_MEAL_CHOICE, default='salad')
    recipe_author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_status = models.BooleanField(default=True)
    recipe_likes = models.IntegerField(default=0)
    recipe_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    recipe_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.recipe_name}'

    class Meta:
        db_table = 'recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'



