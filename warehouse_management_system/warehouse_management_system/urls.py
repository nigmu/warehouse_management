"""
URL configuration for warehouse_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from warehouse.views import warehouse_page, block_page, index
from tile.views import tile_page
from stock.views import stack_page

urlpatterns = [

    #  Default API routes
    path('admin/', admin.site.urls),
    path('api/warehouse/', include('warehouse.urls')),
    path('api/tile/', include('tile.urls')),
    path('api/stack/', include('stock.urls')),

    #  Frontend routes
    path('', index, name='home'),
    path('warehouse/', warehouse_page, name = 'warehouse_page'),
    path('block/', block_page, name='block_page'),
    path('tile/', tile_page, name='tile_page'),
    path('stock/', stack_page, name='stock_page')

    # Search stock by tile name and tile size
    

]
