from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_answer', 'layer_reference')
    list_filter = ('layer_reference',)
