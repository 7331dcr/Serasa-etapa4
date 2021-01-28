import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Aluno, Gabarito, Prova
from . import util

# Create your views here.

def index(request):
    return render( request, "gradesmanager/index.html")

@csrf_exempt
def cadastrar_gabarito(request):
    
    # jeferson = '{[ {"p1":"r1"},{"p2":"r2"},{"p3":"r3"},{"p4":"r4"} ]}'
    # x = '{ "name":"John", "age":30, "city":"New York"}'
    
    # joyce = {[
    #     {"p1":"r1"},
    #     {"p2":"r2"},
    #     {"p3","r3"}
    # ]}
    # joyco = json.dumps(joyce)
    # print(joyco)
    # jenifer = json.loads(jeferson)
    # print(jenifer)


    if request.method != "POST":
        return JsonResponse({"error":"POST request required."}, status=400)

    if request.body == b'' or request.body == None:
            return JsonResponse({"error":"No JSON body"}, status=400)

    payload = json.loads(request.body)
    print(payload['data'])

    for row in payload['data']:
        pergunta = list(row.keys())[0]
        resposta = list(row.values())[0]
        entry = Gabarito(pergunta=pergunta, resposta=resposta)
        try:
            entry.save()
        except:
            return JsonResponse({"error": "Gabarito not saved"}, status=400)

    return JsonResponse({"message": "Data successfully saved"}, status=201)

def cadastrar_resposta(request):
    
    if request.method != "POST":
        return JsonResponse({"error":"POST request required."}, status=400)
    
    if request.body == b'' or request.body == None:
            return JsonResponse({"error":"No JSON body"}, status=400)
    
    # Demands JSON query
    gabarito_id = request.GET.get('gabarito_id', '')
    aluno_id = request.GET.get('aluno_id', '')
    if gabarito_id == '' or aluno_id == '':
        return JsonResponse({
            "error":"Missing queries: 'gabarito_id' and 'aluno_id'"
        }, status=400)

    # Saves payload to database
    payload = json.loads(request.body)
    respostas = Prova(respostas=payload)
    try:
        respostas.save()
    except:
        return JsonResponse({"error": "Resposta not saved"}, status=400)
    
    # Updates "nota" field after saving "respostas" to db
    ## RUN FUNCTION to from util to update the "nota" field



    return False