from django.shortcuts import render
from .models import GameLink

# Create your views here.
def home(request):
    items = GameLink.objects.all()
    return render(request, "home.html", {
        "games": items,
    })

def test(request):
    pass