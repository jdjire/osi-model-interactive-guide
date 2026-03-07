from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('api/questions/', views.get_questions, name='get_questions'),
]
