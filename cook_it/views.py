from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


'''
THE VARS THAT EACH VIEW PASS THROUGH:
(trying to help u out Angel) -JT
HOME: All categories and one recipe (for now, will change if needed)
CATEGORY: A single category
RECIPE: A single recipes
PROFILE: Posted recipes for the user thats signed in
SIGN IN: none needed (i think)
'''


template_paths:dict={
    #'VIEW':'PATH',
    'home':'base.html',
    'category':'base.html',
    'recipe':'base.html',
    'profile':'base.html',
    'logout':'base.html',
}

# ---------- FBVs ----------
def home(request):
    categories= Category.objects.all()
    featured_recipe = Recipe.objects.order_by('-rating').first()
    return render(request, template_paths['home'], {'featured_recipe':featured_recipe, 'categories':categories})

def category(request,category_id):
    category= Category.objects.get(name=category_id)
    return render(request,template_paths['category'],{'category':category})

def recipe(request,recipe_id):
    recipe= Recipe.objects.get(name=recipe_id)
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
        
        return redirect('recipe', recipe_name=recipe.name) 

    return redirect('home')

def logout(request):
    return render(request, template_paths['logout'], {})

# ---------- CBVs ----------
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'








'''# views.py (Corrected template_paths and view logic)

template_paths:dict={
    #'VIEW':'PATH',
    'home':'index.html',
    'category':'food_category.html',
    'recipe':'base.html', # Note: Still needs a dedicated template for recipe detail
    'profile':'profile.html',
    'logout':'logged_out.html',
}

# ...

def category(request,category_id):
    # FIXED: Use id for lookup
    category= Category.objects.get(id=category_id)
    return render(request,template_paths['category'],{'category':category})

def recipe(request,recipe_id):
    # FIXED: Use id for lookup
    recipe= Recipe.objects.get(id=recipe_id)
    return render(request,template_paths['recipe'],{'recipe':recipe})

# ...

@login_required
def add_comment(request, recipe_id):
    if request.method == "POST":
        # ... (comment creation logic)
        
        # FIXED: Redirect using recipe_id
        return redirect('recipe', recipe_id=recipe.id) 

    return redirect('home')
    
    
    
    <div class="category-grid">
                {% for category in categories %}
                <a href="{% url 'category' category.id %}" class="category-item">
                    <img src="{% static 'img/icon_'|add:category.name|lower|add:'.png' %}" alt="{{ category.name }}">
                    <p>{{ category.name }}</p>
                </a>
                {% endfor %}
            </div>
    '''