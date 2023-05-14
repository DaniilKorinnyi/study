from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from .forms import PurchaseForm
from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseSerializer
import django_filters
from rest_framework import filters

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'total_price': ['gte', 'lte', 'gt', 'lt', 'exact']
        }
class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    search_fields = ['user', 'book']
    ordering_fields = ['total_price']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]


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
# def purchase(request):
#     purchase = Purchase.objects.all()
#     data = list(purchase.values())
#     return JsonResponse(data, safe=False)
