from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserForm

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    form_class = UserForm

def simple(request):
    return HttpResponse('Test')

def users(request):
    users = User.objects.all()
    data = list(users.values())
    return JsonResponse(data, safe=False)