from django.urls import path
from .views import (
    MessageCreateView,
)
from . import views

urlpatterns = [
    path('message/new/', MessageCreateView.as_view(), name='message-create')
]