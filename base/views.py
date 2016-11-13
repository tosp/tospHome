from django.shortcuts import render


def home(request):
    return render(request, "base/home.html")

def homeAccess(request):
    return render(request, "base/home_access.html")

def homeNoAccess(request):
    return render(request, "base/home_no_access.html")


def base_files(request, filename):
    location = "base/" + filename
    return render(request, location, {}, content_type="text/plain")
