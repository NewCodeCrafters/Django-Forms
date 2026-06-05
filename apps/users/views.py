from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

from .models import User
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)

                if check_password(password, user.password):
                    request.session["user_id"] = user.id
                    request.session["username"] = user.username
                    request.session["user_type"] = user.user_type

                    user.last_login = timezone.now()
                    user.save()

                    messages.success(request, "Login Completed")

                    # Redirect to ?next= if provided, otherwise b_list
                    next_url = request.POST.get("next") or request.GET.get("next")
                    return redirect(next_url if next_url else "b_list")

                else:
                    messages.error(request, "Incorrect Password")

            except User.DoesNotExist:
                messages.error(request, "User not found")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    request.session.flush()
    messages.success(request, "Logout Successful")
    return redirect("login")


def home(request):
    user_id = request.session.get("user_id")

    if not user_id:
        messages.error(request, "Please login first")
        return redirect("login")

    user = User.objects.get(id=user_id)
    return render(request, "home.html", {"user": user})