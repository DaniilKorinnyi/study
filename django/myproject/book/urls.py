from django.urls import path
from .views import book

urlpatterns = [
    path('', book, name='book'),
]