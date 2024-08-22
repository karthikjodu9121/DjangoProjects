from django.shortcuts import render

# Create your views here.

def app_home(request):
    return render(request, "blogApp/app_home.html", {})

def author_details(request):
    author = {
        'name': 'Karthik',
        'age' : 24,
        'college' : 'RGUKT',
        'skills' : ['Python', 'C', 'C++', 'Java']
    } 
    return render(request, "blogApp/author_details.html", {'author' : author})