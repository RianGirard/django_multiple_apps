from django.shortcuts import render

def register(request):
    print(f"placeholder for users to create a new user record")
    return render(request, "index.html")

def login(request):
    print(f"placeholder for users to log in")
    return render(request, "index.html")

def users(request):
    print(f"placeholder to later display all the list of users")
    return render(request, "index.html")

# Create your views here.
