from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.home_view, name='profile'),
    path('goals/', views.home_view, name='goals'),
    path('customize_diet/', views.home_view, name='customize_diet'),
    path('meal_plan/', views.home_view, name='meal_plan'),
]
