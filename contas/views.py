from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
import datetime


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    data['form'] = form
    return render(request, 'contas/form.html', data)