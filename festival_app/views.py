from django.shortcuts import render

def cadastro(request):
    return render(request, 'festival_app/cadastro.html')