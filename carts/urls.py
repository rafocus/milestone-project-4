from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('cart', view_cart, name='cart'),
    path('ticket/<int:pk>/add/', add_to_cart, name='add-to-cart'),
    path('cart/adjust/<int:pk>/', adjust_cart, name='adjust-cart'),
]