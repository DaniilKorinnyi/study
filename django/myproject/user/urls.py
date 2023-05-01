from django.urls import path
from .views import users, simple, UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('', users, name='users'),
    path('simple', simple, name='simple'),
    path('list', UserListView.as_view(), name='user-list'),
    path('create', UserCreateView.as_view(), name='user-create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='user-detail')

]