from django.test import TestCase
from cook_it.models import *
import datetime



class BaseTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):

        cls.user_a = User.objects.create_user(
            username='user_a', 
            password='password123',
            first_name='Alice'
        )
        cls.user_b = User.objects.create_user(
            username='user_b', 
            password='password123',
            first_name='Bob'
        )
        
        cls.cat_baking = Category.objects.create(name="Baking")
        cls.cat_grilling = Category.objects.create(name="Grilling")
        
        cls.recipe_bread = Recipe.objects.create(
            name="Classic Bread",
            author=cls.user_a,
            cost=5.50,
            cook_time=datetime.time(1, 30, 0), # 1h 30m
            rating=4.0,
            category=cls.cat_baking
        )
        
        cls.recipe_cookies = Recipe.objects.create(
            name="Oatmeal Cookies",
            author=cls.user_a,
            cost=8.00,
            cook_time=datetime.time(0, 20, 0), # 20m
            rating=4.5,
            category=cls.cat_baking
        )

        cls.recipe_steak = Recipe.objects.create(
            name="Grilled Steak",
            author=cls.user_b,
            cost=15.00,
            cook_time=datetime.time(0, 20, 0), # 20m
            rating=4.8,
            category=cls.cat_grilling
        )
        
        cls.ing_flour = Ingredient.objects.create(
            recipe=cls.recipe_bread,
            quantity="500",
            unit="g",
            name="Bread Flour"
        )
        cls.ing_water = Ingredient.objects.create(
            recipe=cls.recipe_bread,
            quantity="300",
            unit="ml",
            name="Water"
        )
        
        cls.inst_1 = Instruction.objects.create(
            recipe=cls.recipe_bread,
            step_number=1,
            description="Mix flour and water."
        )
        cls.inst_2 = Instruction.objects.create(
            recipe=cls.recipe_bread,
            step_number=2,
            description="Knead for 10 minutes."
        )
        
        cls.comment_1 = Comment.objects.create(
            author=cls.user_b,
            recipe=cls.recipe_bread,
            text="Looks delicious!"
        )



class CategoryModelTests(BaseTestCase):
    pass

class RecipeModelTests(BaseTestCase):
    pass

class IngredientModelTests(BaseTestCase):
    pass

class InstructionModelTests(BaseTestCase):
    pass

class CommentModelTests(BaseTestCase):
    pass
