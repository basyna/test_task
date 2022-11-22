from django.contrib import admin
from django.urls import path

from .views import (
    CancelView, CreateCheckoutSessionView, ItemDetail, SuccessView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
