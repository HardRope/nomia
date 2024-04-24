from django.contrib import admin

from .models import CateringType
from .models import Question
from .models import Option

@admin.register(CateringType)
class CateringTypeAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ['text', 'multiple',]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
	list_display = ['text', 'question',]
