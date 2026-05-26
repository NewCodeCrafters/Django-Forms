from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import SignupForm, Loginform

def home(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("login")
    
    user = User.objects.get(id=user_id)

    context = {
        "user": user
    }

    return render(request, "home.html", context)
def signup(request):

    if request.method == "POST":

        form = SignupForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = form.save(commit=False)

            user.password = make_password(
                form.cleaned_data['password']
            )

            user.save()

            messages.success(
                request,
                "Account has been created Successfully"
            )

            return redirect('login')

    else:

        form = SignupForm()

    context = {
        "form": form
    }

    return render(
        request,
        "signup.html",
        context
    )

def login(request):

    if request.method == "POST":

        form = Loginform(request.POST)

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

                    messages.success(
                        request,
                        "Login Completed"
                    )

                    return redirect("home")

                else:
                    messages.error(
                        request,
                        "Incorrect Password"
                    )

            except User.DoesNotExist:

                messages.error(
                    request,
                    "404 User Not Found"
                )

    else:
        form = Loginform()

    context = {
        "form": form
    }

    return render(
        request,
        "login.html",
        context
    )    
def logout(request):
    request.session.flush()

    messages.success(
        request, "logged out successfully"
    )
    return redirect("login")