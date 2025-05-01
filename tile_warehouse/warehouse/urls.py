from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.warehouse_list, name='warehouse_list'),
    path('add/', views.warehouse_add, name='warehouse_add'),
    path('edit/<int:pk>/', views.warehouse_edit, name='warehouse_edit'),
    path('delete/<int:pk>/', views.warehouse_delete, name='warehouse_delete'),
]
