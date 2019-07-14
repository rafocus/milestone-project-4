from django.urls import path
from .views import (
    TicketListView,
    TicketDetailView
)
from . import views

urlpatterns = [
    path('', TicketListView.as_view(), name='main-home'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('about/', views.about, name='main-about'),
]