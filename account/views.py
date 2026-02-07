from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from core.models import taskdata
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
def account(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not User.objects.filter(username=username).exists():
                return render(
                request,
                'signup_login.html',
                {
                    'login_error': 'User not found. Please register first.',
                    'active_tab': 'login'
                }
               )
        
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'signup_login.html',{'login_error':'Invalid Password','active_tab': 'login','login_username': username})
        
        if action == 'signup' :
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')

            if password != password1:
                return render(request,'signup_login.html',{'signup_error':'Password do not match','active_tab': 'signup','signup_username': username,'signup_email': email,})
            if User.objects.filter(username=username):
                return render(request,'signup_login.html',{'signup_error':'User already exists','active_tab': 'signup'})
            if User.objects.filter(email=email):
                return render(request,'signup_login.html',{'signup_error':'Email already used','active_tab': 'signup','signup_username': username,'signup_password': password,'signup_password1': password1})
            user = User.objects.create_user(username=username,email=email,password=password1)
            
            login(request, user)

            return redirect('home')
        
    return render(request,'signup_login.html')

@never_cache
@login_required
def deleteacc(request):
    if request.method == "POST":
        password = request.POST.get("password")
        user = request.user

        if not user.check_password(password):
            messages.error(request, "Incorrect password")
            return redirect("home")

        logout(request)
        user.delete()
        return redirect("publichome")
    return redirect('home')
