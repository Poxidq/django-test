from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def contacts(request):
    return render(request, "pages/contacts.html")

