from django.shortcuts import redirect, render

def index(request):
    print("placeholder to later display a list of all blogs")
    return render(request, "blogs.html")

def new(request):
    print("placeholder to display a new form to create a new blog")
    return render(request, "blogs.html")

def create(request):
    return redirect('/blogs')

def show(request, id):
    print(f"placeholder to display blog number:{id}")
    return render(request, "blogs.html")

def edit(request, id):
    print(f"placeholder to edit blog number:{id}")
    return render(request, "blogs.html")

def destroy(request, id):
    return redirect('/blogs')

# Create your views here.
