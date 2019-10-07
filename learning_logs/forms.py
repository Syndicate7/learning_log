from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields =['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['title','text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols':160})}#Ширина текстовой области составляла 80 столбцов вместо значения по умолчанию 40