"""Определяет схемы URL для пользователей"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
	#Страница входа
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),#, {'template_name': 'users/login.html'}, name='login'),
	path('logout', views.logout_view, name='logout'),
	# Страница регистрации
	path('register', views.register, name='register'),
]

