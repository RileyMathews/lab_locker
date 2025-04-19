from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpRequest, HttpResponse
from lab_locker.models import User
from django.shortcuts import redirect, render


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class SigninForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


def signup_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "auth/signup.html", {"form": form})

def signin_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            maybe_user = authenticate(username=username, password=password)
            if maybe_user is not None:
                return HttpResponse(b"User authenticated successfully.")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = SigninForm()
    return render(request, "auth/signin.html", {"form": form})
