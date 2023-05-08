from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import UserForm
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

class UserPagination(PageNumberPagination):
    page_size = 10

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    page_size_query_param = 'page_size'
    max_page_size = 10
    ordering_fields = ['last_name', 'first_name']
    search_fields = ['age']


# class UserListView(ListView):
#     model = User
#     template_name = 'user_list.html'
#
# class UserDetailView(DetailView):
#     model = User
#     template_name = 'user_detail.html'
#
# class UserCreateView(CreateView):
#     model = User
#     template_name = 'user_form.html'
#     form_class = UserForm

def simple(request):
    return HttpResponse('Test')

def users(request):
    users = User.objects.all()
    data = list(users.values())
    return JsonResponse(data, safe=False)