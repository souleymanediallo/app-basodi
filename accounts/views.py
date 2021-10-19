from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.upper()
            user.save()
            messages.success(request, "Votre compte a été crée !")
            return redirect("home")
    else:
        messages.warning(request, 'Tous les champs sont obligatoires !')
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/register.html", context)


# https://docs.djangoproject.com/fr/3.2/topics/auth/default/

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Erreur email ou mot de passe")

    return render(request, "accounts/login.html")


def dashboard(request):
    return render(request, "accounts/dashboard.html")