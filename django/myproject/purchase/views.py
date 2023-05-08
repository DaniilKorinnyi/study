from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from .forms import PurchaseForm
from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

# class PurchaseListView(ListView):
#     model = Purchase
#     template_name = 'purchase_list.html'
#
# class PurchaseDetailView(DetailView):
#     model = Purchase
#     template_name = 'purchase_detail.html'
#
# class PurchaseCreateView(CreateView):
#     model = Purchase
#     template_name = 'purchase_form.html'
#     form_class = PurchaseForm
def purchase(request):
    purchase = Purchase.objects.all()
    data = list(purchase.values())
    return JsonResponse(data, safe=False)
