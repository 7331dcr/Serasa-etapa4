import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Aluno, Gabarito, Prova

# Create your views here.

def index(request):
    return render( request, "gradesmanager/index.html")

@csrf_exempt
def cadastrar_gabarito(request):
    
    if request.method != "POST":
        return JsonResponse({"error":"POST request required."}, status=400)

    if request.body == b'' or request.body == None:
            return JsonResponse({"error":"No JSON body"}, status=400)

    payload = json.loads(request.body)
    
    gabarito = Gabarito(gabarito=payload)
    try:
        gabarito.save()
    except:
        return JsonResponse({"error": "Gabarito not saved"}, status=400)

    return JsonResponse({"message": "Data successfully saved"}, status=201)

def cadastrar_resposta(request):
    return False