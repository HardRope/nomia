from django.contrib import admin

from .models import CateringType
from .models import Question
from .models import Option
from .models import Result


class QuestionInline(admin.TabularInline):
    model = Question.catering.through


class OptionInline(admin.TabularInline):
    model = Option


@admin.register(CateringType)
class CateringTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'multiple']
    inlines = [OptionInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'question']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']

    def user(self, obj):
        return obj.patricipiant.username
