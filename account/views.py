from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserLoginForm
from django.contrib.auth import get_user_model , authenticate , login , logout
from django.contrib import messages

User = get_user_model()


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            User.objects.create_user(email,password)
            return redirect('login')
        return render(request,'account/register.html',{'form' : form})
    form = UserRegisterForm()
    return render(request,'account/register.html',{'form' : form})



def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email,password=password)
            if not user:
                messages.info(request,'email or password is wrong!')
                return redirect('login')
            login(request,user)
            return redirect('index')
        return render(request , 'account/login.html' , {'form' : form})
    
    form = UserLoginForm()
    return render(request , 'account/login.html' , {'form' : form})


def logout_user(request):
    logout(request)
    return redirect('login')
