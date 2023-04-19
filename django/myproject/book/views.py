from django.shortcuts import render
from .models import Book
from django.http import JsonResponse

# Create your views here.
def book(request):
    books = Book.objects.all()
    data = list(books.values())
    return JsonResponse(data, safe=False)