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

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['get_user', 'text']

    def get_user(self, obj):
        return obj.patricipiant.username
