from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=16)

    recipes: models.manager.Manager['Recipe']
    @property
    def average_cost(self):
        result = self.recipes.aggregate(avg_cost=models.Avg('cost'))
        return result['avg_cost'] or 0.0

    @property
    def average_rating(self):
        result = self.recipes.aggregate(avg_rating=models.Avg('rating'))
        return result['avg_rating'] or 0.0
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name=models.CharField(max_length=64)
    # links to user
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="recipes")
    cost=models.FloatField()
    cook_time=models.TimeField()
    rating=models.FloatField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.name


'''
Both ingredients and Instructions are their own models because they are lists
Using this method compared to just a str (using a textfield)
This way creates structered and relaional data and is more reliable
'''


class Ingredient(models.Model):
    #links to recipe
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    quantity=models.CharField(max_length=24, blank=True)
    unit=models.CharField(max_length=24, blank=True)
    name=models.CharField(max_length=24, blank=True)

    def __str__(self):
        return f'{self.quantity} {self.unit} {self.name}'
    
class Instruction(models.Model):
    # links to recipe
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instructions')
    step_number=models.PositiveIntegerField()
    description=models.TextField()

    # this keeps the instructions in order
    # "Meta" is a 'config blueprint', used for different things
    class Meta:
        ordering=['step_number']

    def __str__(self):
        return f'{self.step_number}. {self.description[:50]}...'
    
class Comment(models.Model):
    # links to a recipe and a user
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    text=models.TextField()

    def __str__(self):
        return f'On {self.recipe.name} {self.author.get_full_name} commented: {self.text[:50]}...'
