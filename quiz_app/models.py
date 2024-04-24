from django.db import models

class CateringType(models.Model):
	name = models.CharField('тип', max_length=25, unique=True)

	class Meta:
		verbose_name = 'заведение'
		verbose_name_plural = 'заведения'

	def __str__(self):
		return self.name


class Question(models.Model):
	text = models.CharField('вопрос', max_length=255)
	multiple = models.BooleanField(default=False)

	catering = models.ManyToManyField(
		'CateringType',
		related_name='questions',
		null=True,
		blank=True)

	class Meta:
		verbose_name = 'вопрос'
		verbose_name_plural = 'вопросы'

	def __str__(self):
		return self.text


class Option(models.Model):
	text = models.CharField('ответ', max_length=255)

	question = models.ForeignKey(
		'Question',
		 on_delete=models.CASCADE,
		 related_name='options',
		 null=True,
		 blank=True,
		 )
	catering = models.ManyToManyField(
		'CateringType',
		related_name='options',
		null=True,
		blank=True,
		)

	class Meta:
		verbose_name = 'ответ'
		verbose_name_plural = 'ответы'

	def __str__(self):
		return self.text
