from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

from main.forms import CreateUserForm


def index(request):
    return render(request,'main/index.html')

def introcsPage(request):
    return render(request,'main/introcs.html')

def exposPage(request):
    return render(request,'main/expos.html')

def DSPage(request):
    return render(request,'main/DS.html')

def physicsPage(request):
    render(request,'main/physics.html')

def chemistryPage(request):
    return render(request,'main/chemistry.html')

def musictheoryPage(request):
    return render(request,'main/musictheory.html')

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

def userHome(request):
    return render(request,'main/userHome.html')

def loginPage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,username)
            return render(request, 'userHome/')
        else:
            messages.info(request, 'Username or password is incorrect')

    context={}
    return render(request,'main/login.html',context)  
   

