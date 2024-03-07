from django.urls import path
from .import views  # Corrected import statement

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
]

