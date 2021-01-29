import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Aluno, Gabarito, Prova, Respostas
from .util import atualizar_nota

def index(request):
    # Renders the API documentation 
    return render(request, "gradesmanager/index.html")

@csrf_exempt
def cadastrar_gabarito(request):
    
    if request.method != "POST":
        return JsonResponse({"error":"POST request required."}, status=400)
    
    if request.body == b'' or request.body == None:
            return JsonResponse({"error":"No JSON body"}, status=400)

    payload = json.loads(request.body)

    prova = Prova(nome_prova=payload['test_name'])
    try:
        prova.save()
    except:
        return JsonResponse({"error": "Faield to add new entry"}, status=400)

    for row in payload['data']:
        pergunta = list(row.keys())[0]
        resposta = list(row.values())[0]
        entry = Gabarito(prova_fk=prova, pergunta=pergunta, resposta=resposta)
        try:
            entry.save()
        except:
            return JsonResponse({"error": "Faield to add new entry"}, status=400)

    return JsonResponse({"message": "Successfully added new entry"}, status=201)


@csrf_exempt
def cadastrar_aluno(request):

    if request.method != "POST":
        return JsonResponse({"error":"POST request required."}, status=400)
    
    if request.body == b'' or request.body == None:
            return JsonResponse({"error":"No JSON body"}, status=400)

    limit = Aluno.objects.all()
    if len(limit) > 100:
        return JsonResponse({"error":"Limit of 100 students reached"}, status=400)

    payload = json.loads(request.body)
    entry = Aluno(nome=payload['student_name'])
    try:
        entry.save()
    except:
        return JsonResponse({"error": "Failed to add new entry"}, status=400)

    return JsonResponse({"message": "Successfully added new entry"}, status=201)


@csrf_exempt
def cadastrar_resposta(request):
    
    if request.method != "POST":
        return JsonResponse({"error":"POST request required."}, status=400)
    
    if request.body == b'' or request.body == None:
            return JsonResponse({"error":"No JSON body"}, status=400)

    payload = json.loads(request.body)

    # Checks if student_id exists in the db
    try:
        aluno = Aluno.objects.get(id=payload['student_id'])
    except:
        return JsonResponse({"error": "'Aluno' not found"}, status=400)
    
    # Checks if test_id exists in the db
    try:
        prova = Prova.objects.get(id=payload['test_id'])
    except:
        return JsonResponse({"error": "'Prova' not found"}, status=400)

    # Saves entries to database
    prova.aluno_fk = aluno
    prova.save()
    for row in payload['data']:
        pergunta = list(row.keys())[0]
        resposta = list(row.values())[0]
        entry = Respostas(prova_fk=prova, pergunta=pergunta, resposta=resposta)
        try:
            entry.save()
        except:
            return JsonResponse({"error": "Faield to add new entry"}, status=400)

    atualizar_nota(prova)

    return JsonResponse({"message": "Successfully added new entry"}, status=201)

def aprovados(request):
    
    if request.method == "GET":

        alunos = Aluno.objects.all()

        for aluno in alunos:
            prova = Prova.objects.filter(aluno_fk=aluno.id)
            quantidade = len(prova)
            somatorio = 0
            nota_final = 0
            
            for row in range(quantidade):
                somatorio = somatorio + prova[row].nota
            
            if somatorio > 0 or quantidade > 0:
                nota_final = somatorio / quantidade
            
            if nota_final > 7:
                aluno.aprovado = True
            else:
                aluno.aprovado = False
            
            print(aluno.aprovado)

    return JsonResponse({"aprovados":"?"})
