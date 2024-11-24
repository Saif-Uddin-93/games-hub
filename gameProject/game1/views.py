from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    items = []
    return render(request, "home.html", {
        "home_items": items,
    })

def test(request):
    items = ["A", "B", "C"]
    return render(request, "test.html", {
        "testItems":items
    })

def react(request):
    items = []
    return render(request, 'game1/index.html', {
        "react_items" : items
    })

def about(request):
    items = []
    return render(request, 'about.html', {
        "about_items" : items
    })

def games(request):
    items = GameLink.objects.all()
    return render(request, "games.html", {
        "games_items": items,
    })

def contact(request):
    items = []
    return render(request, 'contact.html', {
        "contact_items" : items
    })
