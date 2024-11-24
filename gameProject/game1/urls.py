from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('games/', games, name="games"),
    path('contact/', contact, name="contact"),
    path("test/", test, name="test"),
    path("react/", react, name="react")
]
