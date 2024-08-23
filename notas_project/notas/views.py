from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Nota
from .forms import NotaForm
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})

@login_required
def adicionar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/form_nota.html', {'form': form})

@login_required
def atualizar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/form_nota.html', {'form': form})

@login_required
def remover_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('lista_notas')
    return render(request, 'notas/confirma_remocao.html', {'nota': nota})
