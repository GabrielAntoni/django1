from django.shortcuts import render


# Create your views here.

def index(request):
    Apresentação = {
        'Nome': 'Nome: Gabriel Antoni de Moraes Souza',
        'Idade': 'Idade: 25'
    }
    return render(request, 'index.html',Apresentação)


def contato(request):
    return render(request, 'contato.html')
