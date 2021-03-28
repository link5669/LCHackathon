from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

from main.forms import CreateUserForm


def index(request):
    return render(request,'main/index.html')

def registerPage(request):
    form=CreateUserForm()
    
    if request.method == 'POST':
       form =CreateUserForm(request.POST)
       if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
    
    context = {'form':form}

    return render(request,'main/register.html',context)


def loginPage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,username)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context={}
    return render(request,'main/login.html',context)  
   
   

def home(request):
    render(request,'main/userHome.html')


