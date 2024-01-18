from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def httpRegisterUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data["password1"]
            messages.success(request, f"Hey {username}, you account is created successfully.")
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect("main:index") 
        else:
            print(form.errors)
            print("hello")
    else:
        form = UserForm()
    context = {
        "form": form
    }
    return render(request, "auths/registerUser.html", context)