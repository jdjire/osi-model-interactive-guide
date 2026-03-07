from django.contrib import admin
from .models import Protocol

@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('name', 'layer', 'default_port')
    list_filter = ('layer',)
    search_fields = ('name', 'description')
