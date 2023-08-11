from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_page(request):
    logout(request)
    return redirect("/")


def login_page():
    pass


def register_page():
    pass
