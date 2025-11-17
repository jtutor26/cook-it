from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('category/<int:category_id>/', category, name='category'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]