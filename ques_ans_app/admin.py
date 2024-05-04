from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    fk_name = 'question'
    readonly_fields = ('id',)  # Добавляем поле ID в список только для чтения


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    readonly_fields = ('id',)  # Добавляем поле ID в список только для чтения


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
