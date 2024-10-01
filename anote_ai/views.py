from django.shortcuts import render,redirect, HttpResponse
from .models import Anotacao
from .forms import AnotacaoForm
from django.contrib.auth.decorators import login_required


def anotacoes(request):
    dados = {
        'dados': Anotacao.objects.all()
    }
    return render(request,'anotacoes/anotacoes.html', context=dados)

def detalhe(request, id_anotacao):
    dados = {
        'dados':Anotacao.objects.get(pk=id_anotacao)
    }
    return render(request,'anotacoes/detalhe.html',dados)

@login_required
def criar(request):
    if request.method == 'POST':
        anotacao_form = AnotacaoForm(request.POST)
        if anotacao_form.is_valid():
            anotacao_form.save()
        return redirect('anotacoes')  
    else:  
        anotacao_form = AnotacaoForm()
        formulario = {
            'formulario': anotacao_form
        }

        return render(request, 'anotacoes/nova_anotacao.html', context=formulario)
    
@login_required    
def editar(request,id_anotacao):
       anotacao = Anotacao.objects.get(pk=id_anotacao)
       # nova_anotacao/1 --GET
       if request.method == 'GET':
           formulario = AnotacaoForm(instance=anotacao)
           return render(request, 'anotacoes/nova_anotacao.html',{'formulario': formulario})
       # caso requisicao seja POST:
       else:
           formulario = AnotacaoForm(request.POST, instance=anotacao)
           if formulario.is_valid():
               formulario.save()
           return redirect('anotacoes')
       
@login_required       
def excluir(request,id_anotacao):
    anotacao = Anotacao.objects.get(pk=id_anotacao)
    if request.method == 'POST':
        anotacao.delete()
        return redirect('anotacoes')
    return render(request,'anotacoes/confirmar_exclusao.html',{'item':anotacao})       

