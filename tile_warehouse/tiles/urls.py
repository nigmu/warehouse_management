from django.urls import path
from . import views

app_name = 'tiles'

urlpatterns = [
    path('', views.tile_list, name='tile_list'),
    path('add/', views.tile_add, name='tile_add'),
    path('edit/<int:pk>/', views.tile_edit, name='tile_edit'),
    path('delete/<int:pk>/', views.tile_delete, name='tile_delete'),
]
