from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	'''Тема, которую изучает пользователь.'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		'''Возвращает строковое представлении модели.'''
		return self.text

class Entry(models.Model):
	'''Информация изученная пользователем'''
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, null=True)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		if len(self.title) > 50:
			template = '{0.title}'
			return template.format(self)
		else:
			template = '{0.title}'
			return template.format(self)

'''
	def __str__(self):
		if len(self.text) > 50:
			return self.title, self.text[:50] + "..."
		else:
			return self.title, self.text
'''