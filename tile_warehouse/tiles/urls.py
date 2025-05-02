from django.urls import path
from . import views

app_name = 'tiles'

urlpatterns = [
    # TileType
    path('types/',         views.type_list,   name='type_list'),
    path('types/new/',     views.type_create, name='type_create'),
    path('types/<int:pk>/',views.type_detail, name='type_detail'),
    path('types/<int:pk>/edit/',   views.type_update, name='type_update'),
    path('types/<int:pk>/delete/', views.type_delete, name='type_delete'),

    # TileShipment (you already have these)
    path('shipments/',         views.shipment_list,   name='shipment_list'),
    path('shipments/new/',     views.shipment_create, name='shipment_create'),
    path('shipments/<int:pk>/',views.shipment_detail, name='shipment_detail'),
    path('shipments/<int:pk>/edit/', views.shipment_update, name='shipment_update'),
    path('shipments/<int:pk>/delete/', views.shipment_delete, name='shipment_delete'),

    # TileStockLocation
    path('stock/',         views.stock_list,   name='stock_list'),
    path('stock/new/',     views.stock_create, name='stock_create'),
    path('stock/<int:pk>/',views.stock_detail, name='stock_detail'),
    path('stock/<int:pk>/edit/',   views.stock_update, name='stock_update'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
]
