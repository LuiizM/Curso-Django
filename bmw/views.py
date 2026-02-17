from django.http import HttpResponse
from django.shortcuts import render # Ele le o arquivo e renderiza ele 

# Create your views here.
def home(request):
    return render(request, 'bmw\pages\home.html', context={
        "name": "Luiz Octavio"
    })
