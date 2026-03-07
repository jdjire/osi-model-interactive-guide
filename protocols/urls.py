from django.urls import path
from . import views

urlpatterns = [
    path('', views.protocol_explorer, name='protocol_explorer'),
    path('api/protocols/', views.get_protocols, name='get_protocols'),
]
