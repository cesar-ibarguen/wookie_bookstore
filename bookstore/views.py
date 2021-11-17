from django.shortcuts import render
from .models import Book



def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/home.html', context )

def about(request):
    return render(request, 'bookstore/about.html', {'title': 'About'} )