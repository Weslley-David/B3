from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from my_wallet.models import Investidor

def user_signup(request):
    return render(request, template_name='accounts/user_signup.html')


def user_register(request):
    username = request.POST['inputUsername']
    email = request.POST['inputEmail']
    password1 = request.POST['inputPassword1']
    password2 = request.POST['inputPassword2']
    investidor = request.POST['inputInvestidor']
    print(investidor, '\n\n\n\n\n\n\n')

    errors = 0
    error_messages = []
    if password1 != password2:
        errors += 1
        error_messages.append('passwords do not match')
    if User.objects.filter(email=email).exists():
        errors += 1
        error_messages.append('username already exists')
    context = {
        'error_messages': error_messages,
    }

    if errors == 0:
        user = User.objects.create_user(username=username, password=password1, email=email)
        investidor = Investidor(user=user, perfil=investidor)
        investidor.save()
        print(investidor)

    else:
        return render(request, template_name='accounts/user_signup.html', context=context)
    return redirect('index')


def user_login(request):
    username = request.POST['inputUsername']
    password = request.POST['inputPassword']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print('usuario logado com sucesso')
        # redireciona para o valor de 'next' caso a url possua o parametro 'next',
        # caso contrario redireciona para o a url de nome 'index'
        return redirect(request.GET.get('next', 'index'))
    else:
        print('erro de usuario ou password')
        return redirect('user_signin')

def user_signin(request):
    return render(request, template_name='accounts/user_signin.html')


def user_logout(request):
    logout(request)
    return redirect('index')
