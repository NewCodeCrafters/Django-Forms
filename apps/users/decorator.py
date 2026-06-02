from django.shortcuts import redirect
from django.contrib import messages

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("user_id"):

            messages.error(
                request, "Please login"
            )

            return redirect("login")
        return view_func(
            request,
            *args,
            **kwargs
        )
    return wrapper
       