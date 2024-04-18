from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader

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

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
