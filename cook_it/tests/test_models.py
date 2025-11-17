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

'''
sorry its a bit overkill, but i'm just practing the test cases
literally testing everything lmao
-JT
'''
class CategoryModelTests(BaseTestCase):
    def test_str(self):
        self.assertEqual(str(self.cat_baking), "Baking")
    def test_avg_cost(self):
        self.assertAlmostEqual(self.cat_baking.average_cost,6.75)
    def test_avg_raiting(self):
        self.assertAlmostEqual(self.cat_baking.average_rating, 4.25)
    def test_recipes(self):
        self.assertCountEqual(self.cat_baking.recipes.all(), (self.recipe_bread, self.recipe_cookies))

class RecipeModelTests(BaseTestCase):
    def test_str(self):
        self.assertEqual(str(self.recipe_bread), 'Classic Bread')
    def test_name(self):
        self.assertEqual(self.recipe_bread.name, 'Classic Bread')
    def test_author(self):
        self.assertEqual(self.recipe_bread.author, self.user_a)
    def test_cost(self):
        self.assertEqual(self.recipe_bread.cost, 5.50)
    def test_cook_time(self):
        pass
    def test_raiting(self):
        pass
    def test_category(self):
        pass
    def test_ingredients(self):
        pass
    def test_instructions(self):
        pass

class IngredientModelTests(BaseTestCase):
    def test_str(self):
        pass
    def test_recipe(self):
        pass
    def test_quantity(self):
        pass
    def test_unit(self):
        pass
    def test_name(self):
        pass

class InstructionModelTests(BaseTestCase):
    def test_str(self):
        pass
    def test_order(self):
        pass
    def test_step_number(self):
        pass
    def test_description(self):
        pass

class CommentModelTests(BaseTestCase):
    def test_str(self):
        pass
    def test_author(self):
        pass
    def test_recipe(self):
        pass
    def test_text(self):
        pass