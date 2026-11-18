from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from account.forms import LoginForm, RegisterForm

# Create your views here.
def register(request: HttpRequest):
    form = RegisterForm()

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('login')
    return render(
        request,
        'register.html',
        {'form':form}
    )

def login_user(request: HttpRequest):
    form = LoginForm()

    if request.method == "POST":

        if form.is_valid():
            username = form.username.data
            password = form.password.bound_data
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('home')
            else:
                return render(
                request,
                'login.html',
                {'form':form}
                )

    return render(
        request,
        'login.html',
        {'form':form}
    )
