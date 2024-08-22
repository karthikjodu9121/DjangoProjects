from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Post

def home(request):
    name = 'Navadeep'
    return render(request, 'index.html', {'name' : name})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})

def blog(request):
    posts = Post.objects.all().filter(is_published = True)
    return render(request, "blog.html", {'posts' : posts})

    #return redirect(<viewName>)