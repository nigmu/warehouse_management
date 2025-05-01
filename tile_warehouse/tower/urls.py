from django.urls import path
from . import views

app_name = 'tower'

urlpatterns = [
    path('', views.tower_list, name='tower_list'),
    path('add/', views.tower_add, name='tower_add'),
    path('edit/<int:pk>/', views.tower_edit, name='tower_edit'),
    path('delete/<int:pk>/', views.tower_delete, name='tower_delete'),
]
