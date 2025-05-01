from django.urls import path
from . import views

app_name = 'floor'

urlpatterns = [
    path('', views.floor_list, name='floor_list'),
    path('add/', views.floor_add, name='floor_add'),
    path('edit/<int:pk>/', views.floor_edit, name='floor_edit'),
    path('delete/<int:pk>/', views.floor_delete, name='floor_delete'),
]
