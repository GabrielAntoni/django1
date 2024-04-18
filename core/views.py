from django.shortcuts import render

from .models import Certificado
# Create your views here.


def index(request):
    Certificados = Certificado.objects.all()

    Apresentação = {
        'Nome': 'Nome: Gabriel Antoni de Moraes Souza',
        'Idade': 'Idade: 25',
        'Certificados': Certificados
    }
    return render(request, 'index.html',Apresentação)


def contato(request):
    return render(request, 'contato.html')
