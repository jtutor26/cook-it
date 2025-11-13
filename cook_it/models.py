from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#------------------------------Recipe Model------------------------------

'''
Both ingredients and Instructions are their own models because they are lists
Using this method compared to just a str (using a textfield)
This way creates structered and relaional data and is more reliable
'''

class Recipe(models.Model):
    name=models.CharField(max_length=64)
    # links to user
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="recipes")
    cost=models.FloatField()
    cook_time=models.TimeField()
    rating=models.FloatField()

    def __str__(self):
        return self.name

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
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instructions')
    step_number = models.PositiveIntegerField()
    description = models.TextField()

    # this keeps the instructions in order
    # its a 'config blueprint', used for different things
    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f'{self.step_number}. {self.description[:50]}...'