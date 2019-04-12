from django.shortcuts import render, redirect
from .models import Registro_de_chamados
from .forms import Chamados_form


def List_chamados(request):
    data = []

    Lista_chamados_tuple = Registro_de_chamados.objects.values_list('numero_salt','data_envio','time','hashtags','situacoes','colaborador').order_by('-data_envio','-id_chamado')
    for i in Lista_chamados_tuple:
        campo_unitario = list(i)
        data.append(campo_unitario)
    return render(request, 'relatorio.html', {'data': data})


def Cadastro_chamados(request):
    form = Chamados_form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Cadastro_chamados')

    return render(request, 'cadastro_salt.html', {'form': form})
