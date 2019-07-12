from django.shortcuts import render

tickets = [
    {
        'id': '1',
        'author': 'user1',
        'title': 'ticket 1',
        'description': 'this is a ticket 1',
        'date': '12 July 2019',
    },
    {
        'id': '2',
        'author': 'user2',
        'title': 'ticket 2',
        'description': 'this is a ticket 2',
        'date': '11 July 2019',
    }
]

# Create your views here.
def home(request):
    context = {
        'tickets': tickets
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')