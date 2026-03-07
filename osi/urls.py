from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/layer/<int:layer_number>/', views.layer_detail, name='layer_detail'),
    path('comparison/', views.comparison, name='comparison'),
    path('simulation/', views.simulation, name='simulation'),
    path('interview/', views.interview, name='interview'),
]
