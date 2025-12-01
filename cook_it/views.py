from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Category, Recipe, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RecipeForm, IngredientFormSet, InstructionFormSet
import datetime
from django.db import transaction




template_paths: dict = {
    # 'VIEW':'PATH',
    'home': 'index.html',
    'category': 'food_category.html',
    'recipe': 'recipe.html',
    'profile': 'profile.html',
    'add_recipe': 'recipe_form.html',
}

# ---------- FBVs ----------
def home(request):
    categories= Category.objects.all()
    featured_recipe = Recipe.objects.order_by('-rating').first()
    return render(request, template_paths['home'], {'featured_recipe':featured_recipe, 'categories':categories})

def category(request,category_id):
    category= get_object_or_404(Category, id=category_id)
    return render(request,template_paths['category'],{'category':category})

def recipe(request,recipe_id):
    recipe= get_object_or_404(Recipe, id=recipe_id)
    return render(request,template_paths['recipe'],{'recipe':recipe})

@login_required
def profile(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request,template_paths['profile'],{'posted_recipes':recipes})

@login_required
def add_comment(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        Comment.objects.create(
            author=request.user,
            recipe=recipe,
            text=request.POST['comment_text'] 
        )
        
        return redirect('recipe', recipe_id=recipe.id) 

    return redirect('recipe', recipe_id=recipe_id)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        new_recipe = form.save(commit=False)
        ingredient_formset = IngredientFormSet(request.POST, instance=new_recipe, prefix='ingredients')
        instruction_formset = InstructionFormSet(request.POST, instance=new_recipe, prefix='instructions')
        if form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
            new_recipe.author = request.user
            minutes = form.cleaned_data.get('cook_time')
            hours, mins = divmod(minutes, 60)
            new_recipe.cook_time = datetime.time(hour=hours % 24, minute=mins)
            new_recipe.save()
            ingredient_formset.save()
            instructions = instruction_formset.save(commit=False)
            for i, instruction in enumerate(instructions, 1):
                instruction.step_number = i
                instruction.save()
            return redirect('recipe', recipe_id=new_recipe.id)
    else:
        form = RecipeForm()
        ingredient_formset = IngredientFormSet(prefix='ingredients')
        instruction_formset = InstructionFormSet(prefix='instructions')

    return render(request, template_paths['add_recipe'], {'form': form, 'ingredient_formset': ingredient_formset, 'instruction_formset': instruction_formset})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# ---------- CBVs ----------
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'