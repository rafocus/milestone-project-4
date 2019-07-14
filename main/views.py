from django.shortcuts import render
from .models import Ticket
from django.views.generic import ListView, DetailView


class TicketListView(ListView): # generic list view, variable passed is object_list
    model = Ticket
    ordering = ['-date']

class TicketDetailView(DetailView): #generic detail view, variable passed is object
    model = Ticket

def about(request):
    return render(request, 'main/about.html')