from django.contrib import admin

# Register your models here.
from .models import Category, Recipe, Ingredient, Instruction, Comment

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(Comment)
