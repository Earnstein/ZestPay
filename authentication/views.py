from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def httpRegisterUser(request):
    """
    View for user registration. Validates the form, creates a user, and sends a verification email.
    """
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("main:index")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"{username} account is created.")
            return redirect("auths:index") 
        else:
            print(form.errors)
            print("hello")
    else:
        form = UserForm(label_suffix="")
    context = {
        "form": form
    }
    return render(request, "auths/registerUser.html", context)


def httpLogin(request):
    """
    View for user login. Authenticates the user and redirects to the user's account page.
    """
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("main:index")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        email = email.lower()
        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(request, "Invalid login credentials")
            return redirect("main:index")
        
        login(request, user)
        messages.success(request, "You are logged in")
        return redirect("main:index")    
    return render(request, "auths/login.html")
        


def httpLogout(request):
    """
    View for user logout. Logs the user out and redirects to the login page.
    """
    logout(request)
    messages.info(request, "you are logged out")
    return redirect("auths:index")