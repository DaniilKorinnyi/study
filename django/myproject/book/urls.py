from django.urls import path
# from .views import book, BookListView, BookDetailView, BookCreateView
from rest_framework.routers import SimpleRouter
from .views import BookViewSet

urlpatterns = [
    # path('', book, name='book'),
    # path('list', BookListView.as_view(), name='book-list'),
    # path('create', BookCreateView.as_view(), name='book-create'),
    # path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail')
]


router = SimpleRouter()
router.register('', BookViewSet)


urlpatterns += router.urls