from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as authlogin ,authenticate,logout as lg
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save() 
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)  

def login(request):
    if request.method == 'POST':
        print("mal")
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password :
            user = authenticate(username = username, password = password)
            if user:
                authlogin(request, user)
                return redirect('home')
            else :
                return HttpResponse("wrong password")
    else:  
        form = AuthenticationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)

def home(request):
    if request.user.is_authenticated:
        return render(request,"ho.html")
    else :
        return redirect("login")

def logout(request):
    lg(request)
    return redirect("login")
