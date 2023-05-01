from django.urls import path
from .views import purchase, PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    path('', purchase, name='purchase'),
    path('list', PurchaseListView.as_view(), name='purchase-list'),
    path('create', PurchaseCreateView.as_view(), name='purchase-create'),
    path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail')
]