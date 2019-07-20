from django.urls import path
from .views import cart_home

urlpatterns = [
    path('cart', cart_home, name='cart'),
]