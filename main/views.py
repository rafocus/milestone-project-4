from django.shortcuts import render
from .models import Ticket



# Create your views here.
def home(request):
    context = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')