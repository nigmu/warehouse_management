from django.urls import path
from . import views

urlpatterns = [
    # Define your app's URLs here, e.g., a simple home page
    path('', views.home, name='home'),
]
