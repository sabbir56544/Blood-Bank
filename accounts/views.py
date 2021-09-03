from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserCreateForm
from django.contrib import messages
from .decorators import unauthenticated_user
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
 

@unauthenticated_user
def log_in_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            context = {
                'form': form,
                'error': "Invalid Username or Password!!",
            }
            return render(request, 'accounts/login.html', context)

    context = {

    }
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def sign_up_view(request):
    form = UserCreateForm()

    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            subject = "Welcome to Y-Gaming BD"
            message = f"Hi {user.username}, thanks for register Ygaming-BD"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list, fail_silently=True)
            
            return redirect('log-in')

          
        # messages.warning(request, "This Username or email already exist plz try again or password didn't match")
        
    context = {
        'form': form,
        'error': "This Username is already taken",
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def log_out_view(request):
    logout(request)
    return redirect('log-in')