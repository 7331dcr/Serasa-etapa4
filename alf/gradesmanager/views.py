from django.shortcuts import render

# Create your views here.

def index(request):
    return render( request, "gradesmanager/index.html")

def cadastrar_gabarito(request):
    return False

def cadastrar_resposta(request):
    return False