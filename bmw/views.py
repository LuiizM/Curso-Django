from django.http import HttpResponse
from django.shortcuts import render # Ele le o arquivo e renderiza ele 

# Create your views here.
def home(request):
    return render(request, 'bmw/home.html')

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return HttpResponse('CONTATO')