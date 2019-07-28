from django.urls import path
from .views import (
    TicketListView,
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView,
)
from . import views

urlpatterns = [
    path('', TicketListView.as_view(), name='main-home'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket-detail'),
    path('ticket/<int:pk>/vote', views.votetoggle, name='vote'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket-update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket-delete'),
    path('about/', views.about, name='main-about'),
    path('search/', views.search_tickets, name='search')
]