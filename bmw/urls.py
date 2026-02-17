from django.urls import path
from bmw.views import home

urlpatterns = [
    path('', home),
]