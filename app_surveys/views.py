from django.shortcuts import render

def index(request):
    print(f"placeholder to display all the surveys created")
    return render(request, "surveys.html")

def new(request):
    print(f"placeholder for users to add a new survey")
    return render(request, "surveys.html")

# Create your views here.
