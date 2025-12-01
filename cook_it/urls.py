from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # App-specific views
    path('', home, name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('add_recipe/', add_recipe, name='add_recipe'),

    # Authentication views
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_view, name='logout'), 

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
