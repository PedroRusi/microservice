from django.urls import path

from .views import ProductListView, StorageListView, StorageRetrieveAPIView

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('storages', StorageListView.as_view()),
    path('storages/<int:pk>', StorageRetrieveAPIView.as_view())
]
