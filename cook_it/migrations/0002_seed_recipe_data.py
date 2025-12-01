from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_seed_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Category = apps.get_model('cook_it', 'Category')
    Recipe = apps.get_model('cook_it', 'Recipe')
    Ingredient = apps.get_model('cook_it', 'Ingredient')
    Instruction = apps.get_model('cook_it', 'Instruction')

    # --- Create a default user ---
    if User.objects.filter(is_superuser=True).exists():
        author = User.objects.filter(is_superuser=True).order_by('pk').first()
    else:
        author, _ = User.objects.get_or_create(
            username='chef_default',
            defaults={
                'first_name': 'Default',
                'last_name': 'Chef',
                'email': 'chef@example.com',
                'password': make_password('defaultpassword123'),
                'is_staff': False,
                'is_superuser': False,
            }
        )

    # --- Create Categories ---
    category_italian, _ = Category.objects.get_or_create(name='Italian')
    category_mexican, _ = Category.objects.get_or_create(name='Mexican')
    category_dessert, _ = Category.objects.get_or_create(name='Desserts')

    # --- Create Recipe 1: Spaghetti Carbonara ---
    recipe1, created = Recipe.objects.get_or_create(
        name='Spaghetti Carbonara',
        defaults={
            'author': author,
            'category': category_italian,
            'cook_time': '00:30:00',
            'rating': 4.8,
            'cost': 15.00
        }
    )
    
    if created:
        Ingredient.objects.create(recipe=recipe1, quantity='200', unit='g', name='Spaghetti')
        Ingredient.objects.create(recipe=recipe1, quantity='100', unit='g', name='Pancetta or Guanciale')
        Ingredient.objects.create(recipe=recipe1, quantity='2', unit='large', name='eggs')
        Ingredient.objects.create(recipe=recipe1, quantity='50', unit='g', name='Pecorino Romano cheese')
        Ingredient.objects.create(recipe=recipe1, quantity='', unit='', name='Black pepper')

        Instruction.objects.create(recipe=recipe1, step_number=1, description='Boil water for pasta. Add salt and cook spaghetti until al dente.')
        Instruction.objects.create(recipe=recipe1, step_number=2, description='While pasta cooks, fry the pancetta in a pan until crisp. Turn off heat.')
        Instruction.objects.create(recipe=recipe1, step_number=3, description='In a bowl, whisk eggs and grated cheese. Season with lots of black pepper.')
        Instruction.objects.create(recipe=recipe1, step_number=4, description='Drain the pasta, reserving a cup of pasta water. Add the hot pasta to the pan with the pancetta.')
        Instruction.objects.create(recipe=recipe1, step_number=5, description='Quickly pour the egg and cheese mixture over the pasta, stirring vigorously to create a creamy sauce. If it\'s too thick, add a splash of pasta water. Serve immediately.')

    # --- Create Recipe 2: Classic Guacamole ---
    recipe2, created = Recipe.objects.get_or_create(
        name='Classic Guacamole',
        defaults={
            'author': author,
            'category': category_mexican,
            'cook_time': '00:10:00',
            'rating': 4.5,
            'cost': 8.00
        }
    )

    if created:
        Ingredient.objects.create(recipe=recipe2, quantity='3', unit='', name='ripe avocados')
        Ingredient.objects.create(recipe=recipe2, quantity='1/2', unit='', name='red onion, finely chopped')
        Ingredient.objects.create(recipe=recipe2, quantity='1-2', unit='', name='serrano chiles, finely chopped')
        Ingredient.objects.create(recipe=recipe2, quantity='1/2', unit='cup', name='cilantro, chopped')
        Ingredient.objects.create(recipe=recipe2, quantity='1', unit='', name='lime, juiced')
        Ingredient.objects.create(recipe=recipe2, quantity='', unit='', name='Salt to taste')

        Instruction.objects.create(recipe=recipe2, step_number=1, description='Cut the avocados in half, remove the pit, and scoop the flesh into a bowl.')
        Instruction.objects.create(recipe=recipe2, step_number=2, description='Mash the avocado with a fork to your desired consistency (chunky or smooth).')
        Instruction.objects.create(recipe=recipe2, step_number=3, description='Add the chopped onion, chiles, cilantro, and lime juice to the bowl.')
        Instruction.objects.create(recipe=recipe2, step_number=4, description='Stir everything together and season with salt. Taste and adjust seasoning if necessary.')
        Instruction.objects.create(recipe=recipe2, step_number=5, description='Serve immediately with tortilla chips.')

def reverse_seed_data(apps, schema_editor):
    Recipe = apps.get_model('cook_it', 'Recipe')
    Recipe.objects.filter(name__in=['Spaghetti Carbonara', 'Classic Guacamole']).delete()
    
    Category = apps.get_model('cook_it', 'Category')
    Category.objects.filter(name__in=['Italian', 'Mexican', 'Desserts']).delete()

    User = apps.get_model('auth', 'User')
    User.objects.filter(username='chef_default').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('cook_it', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_seed_data, reverse_code=reverse_seed_data),
    ]
