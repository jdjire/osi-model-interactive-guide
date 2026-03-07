from django.contrib import admin
from .models import Layer, InterviewQuestion

@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    list_display = ('layer_number', 'name')
    ordering = ('-layer_number',)

@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
