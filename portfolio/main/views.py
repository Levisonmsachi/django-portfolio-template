from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """View function for home page"""
    return render(request, 'main/home.html')

def about(request):
    """View function for about page"""
    return render(request, 'main/about.html')

def projects(request):
    """View function for projects page"""
    # You can pass data to templates!
    my_projects = [
        {'name': 'Portfolio Website', 'description': 'This website!'},
        {'name': 'Blog App', 'description': 'A simple blog application'},
        {'name': 'Task Manager', 'description': 'Manage daily tasks'},
    ]
    return render(request, 'main/projects.html', {'projects': my_projects})

def contact(request):
    """View function for contact page"""
    return render(request, 'main/contact.html')

def custom_404(request, exception):
    """ Custom 404 error handler """
    return render(request, 'main/404.html', status=404)