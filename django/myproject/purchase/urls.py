from django.urls import path
# from .views import purchase, PurchaseListView, PurchaseDetailView, PurchaseCreateView
from rest_framework.routers import SimpleRouter
from .views import PurchaseViewSet
urlpatterns = [
    # path('', purchase, name='purchase'),
    # path('list', PurchaseListView.as_view(), name='purchase-list'),
    # path('create', PurchaseCreateView.as_view(), name='purchase-create'),
    # path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail')
]

router = SimpleRouter()
router.register('', PurchaseViewSet)


urlpatterns += router.urls
