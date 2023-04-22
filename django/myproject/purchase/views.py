from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Purchase

def purchase(request):
    purchase = Purchase.objects.all()
    data = list(purchase.values())
    return JsonResponse(data, safe=False)
