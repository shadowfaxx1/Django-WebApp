from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post




@login_required  # Ensure login URL is correctly specified
def index(request):
    
    context = {
        'posts' :   Post.objects.all()
    }
    return render(request,'index.html',context)
    
def user_signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password == repassword:
            try:
                user= User.objects.create_user(username,email,password)
                user.save()
                login(request,user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request,'signup.html' ,{'error_message':error_message})
        else:
            error_message = "password do not match"
            return render(request,'signup.html' ,{'error_message':error_message})
    return render(request, 'signup.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html' , {'error_message' : 'Username or Password Invalid'})
    return render(request ,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_about(request):
    print('3')
    return render(request,'about.html',{'error message': '<h1> Page Error </h1>'})