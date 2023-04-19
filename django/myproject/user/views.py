from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User

def users(request):
    users = User.objects.all()
    data = list(users.values())
    return JsonResponse(data, safe=False)