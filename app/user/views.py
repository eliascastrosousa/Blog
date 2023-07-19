from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as auth
from django.contrib.auth import logout, authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(request):
        if request.method == "GET":
            return render(request, 'login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                print(user)
                login_django(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Usuario ou Senha invalidos.'})

def register(request):
            if request.method == "GET":
                return render(request, 'register.html')
            else:
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                password02 = request.POST.get('password02')
                print('entrou no else')
                print(first_name, last_name, username, email, password, password02)

                user = auth.objects.filter(username=username).first()

                if user:
                    return render(request, 'register.html', {'error': 'ja existe um usuario com esse username'})
                elif password != password02:
                    return render(request, 'register.html', {'error': 'Senhas não coincidem'})
                else:
                    user = auth.objects.create_user(first_name = first_name, 
                                                    last_name=last_name, 
                                                    username=username, 
                                                    email = email, 
                                                    password=password)
                    user.save()
                    return redirect(login)


def signout(request):
    logout(request)
    return redirect("login")

def perfil(request):
    return render(request, 'perfil.html')