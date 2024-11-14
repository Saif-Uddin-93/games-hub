from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path("test/", test, name="test"),
    path("react/", react, name="react")
]
