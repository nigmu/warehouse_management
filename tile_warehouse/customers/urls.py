from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='customer_list'),                     # 🔍 View all customers
    path('add/', views.add_customer, name='add_customer'),                   # ➕ Add a new customer
    # path('<int:pk>/', views.customer_detail, name='customer_detail'),        # 📄 View a single customer
    path('<int:pk>/edit/', views.edit_customer, name='edit_customer'),       # ✏️ Edit customer
    path('<int:pk>/delete/', views.delete_customer, name='delete_customer'), # ❌ Delete customer
]
