from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    items = GameLink.objects.all()
    return render(request, "home.html", {
        "games": items,
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