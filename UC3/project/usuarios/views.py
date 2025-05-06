from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm


# Create your views here.

def login(request):
    return render(
        request,
        'login.html'
    )
    
def criarUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        #Será criada um objeto Usuario(model) com os dados enviados
        if form.is_valid(): # se os dados forem validados, são salvos no BD.
            form.save()
            return redirect('/usuario/login')   
    
    else: 
        # se a requisão for get, exibir o formulário de cadastro
        form  = UsuarioForm()
    
    return render(
        request,
        'cadastro.html',
        {'form':form}
    )