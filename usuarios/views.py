from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def cadastrar_usuario(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecionar para a página de login após o cadastro
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})

@login_required
def painel_controle(request):
    user = request.user
    return render(request, 'usuarios/painel_controle.html', {'user': user})