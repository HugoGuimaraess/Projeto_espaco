from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
# Create your views here.



def index(request):
    if not request.user.is_authenticated:
        messages.error(request,f'Deve estar logado para acessar')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data').filter(publicada=True)

    return render(request,'galeria/index.html',{'cards':fotografias})




def imagem(request,foto_id):
    if not request.user.is_authenticated:
        messages.error(request,f'Deve estar logado para acessar')
        return redirect('login')


    fotografia= get_object_or_404(Fotografia,pk=foto_id)


    return render(request,'galeria/imagem.html',{'fotografia':fotografia})



def buscar(request):
    fotografias = Fotografia.objects.order_by('data').filter(publicada=True)

    if 'buscar' in request.GET:
        busca = request.get['buscar']
        fotografias = fotografias.filter(nome__icontains=busca)




    return render(request,'galeria/index.html',{'cards':fotografias})



def editar_imagem(request,foto_id):
    if not request.user.is_authenticated:
        messages.error(request,'Necessário logar')
        return redirect('login')
    form = FotografiaForms(instance=Fotografia)
    fotografia=Fotografia.objects.get(id=foto_id)
    if request.method == 'POST':
        form=FotografiaForms(request.POST,request.FILES,instance=Fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')
    return render(request,'galeria/editar_imagem.html',{'form':form})
def deletar_imagem(request,foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Necessário logar')
        return redirect('login')

    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request,'Fotgrafia deletada com sucesso')
    return redirect('index')

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Necessário logar')
        return redirect('login')

    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Fotografia cadastrada com sucesso')
            return redirect('index')

    return render(request,'galeria/nova_imagem.html',{'form':form})



def filtro(request,categoria):
    fotografias = Fotografia.objects.order_by('data').filter(publicada=True,categoria=categoria)

    return render(request,'galeria/filtro.html',{'cards':fotografias})

