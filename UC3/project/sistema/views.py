from django.shortcuts import render

def index(request):
    return render (
        request,
        'sistema/sistema.html',
    )
    
def apresentacao(request):
    return render (
        request,
        'sistema/apresentacao.html',
    )
    