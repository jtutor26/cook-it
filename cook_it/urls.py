from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('category/<int:category_id>/', category, name='category'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    
]

'''from django.urls import path, include
from django.contrib.auth import views as auth_views # Added for specific auth views
from .views import *

urlpatterns = [
    # Custom Views
    path('', home, name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('category/<int:category_id>/', category, name='category'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),

    # Authentication Views (Overriding 'django.contrib.auth.urls')
    # Use Django's built-in view but give it your custom URL name
    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='forgot_password'),
    
    # Keeping only the necessary default auth paths.
    # Note: If your app requires a full password reset, you will need to add 
    # the 'done', 'confirm', and 'complete' paths back with the corresponding templates.
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]'''
