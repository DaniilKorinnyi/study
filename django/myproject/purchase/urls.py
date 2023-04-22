from django.urls import path
from .views import purchase

urlpatterns = [
    path('', purchase, name='purchase'),
]