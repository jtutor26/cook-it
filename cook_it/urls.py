from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('category/<int:category_id>/', category, name='category'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('accounts/profile/', profile, name='profile'),
]