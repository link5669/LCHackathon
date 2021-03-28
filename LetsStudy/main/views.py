from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory

from main.forms import CreateUserForm


def home(request):
    return render(request,'main/home.html')

def registerPage(request):
    form=CreateUserForm()
    
    if request.method == 'POST':
       form =CreateUserForm(request.POST)
       if form.is_valid():
            form.save() 
    
    context = {'form':form}

    return render(request,'main/register.html',context)


