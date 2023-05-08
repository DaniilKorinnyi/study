from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import BookForm
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book_detail.html'
#
# class BookCreateView(CreateView):
#     model = Book
#     template_name = 'book_form.html'
#     form_class = BookForm

def book(request):
    books = Book.objects.all()
    data = list(books.values())
    return JsonResponse(data, safe=False)