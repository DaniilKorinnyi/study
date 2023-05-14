from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import BookForm
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
import django_filters
from rest_framework import filters

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'author': ['gte', 'lte', 'gt', 'lt', 'exact']
        }
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['author']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

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