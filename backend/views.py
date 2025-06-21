from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def navigation(request):
    return render(request, "navigation.html")