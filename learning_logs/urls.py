'''Определяет схемы URL для learning_logs.'''
#from django.conf.urls import url --- instead put code below...
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
	#Homepage
	path('', views.index, name='index'),
	#Вывод всех тем.
	path('topics/', views.topics, name='topics'),
	#Страница с подробной информацией по отдельной теме.
	#path('topics/(?P<topic_id>\d+)', views.topic, name='topic'), --- Код ДО версии Django 2.0
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#Страница добавения новой темы
	path('new_topic/', views.new_topic, name='new_topic'),
	#Страница для добавления новой записи.
	path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
	#Страница для редактирования записи.
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]