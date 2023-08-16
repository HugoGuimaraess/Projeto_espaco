from django.shortcuts import render,redirect
from apps.usuarios.forms import LoginForms,CadastroForms
from django.contrib import auth,messages
from django.contrib.auth.models import User

def login(request):
    form=LoginForms()

    if request.method == 'POST':
        form=LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha

            )

            if usuario is not None:
                auth.login(request,usuario)
                messages.success(request,'Usuário Logado com sucesso')
                return redirect('index')
            else:
                messages.error(request,'Erro ao logar')
                return redirect('login')

    return render(request,'usuario/login.html',{'form':form})






def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form=CadastroForms(request.POST)
        if form.is_valid():
            nome=form['nome_cadastro'].value()
            senha=form['senha2'].value()
            email=form['email'].value()


            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já existe')
                return redirect('cadastro')


            usuario = User.objects.create_user(
                username=nome,
                password=senha,
                email=email

            )
            usuario.save()

            messages.success(request,'Usuário criado com sucesso')
            return redirect('login')




    return render(request,'usuario/cadastro.html',{'form':form})





def logout(request):
    auth.logout(request)
    messages.success(request,'logout com sucesso')
    return redirect('login')