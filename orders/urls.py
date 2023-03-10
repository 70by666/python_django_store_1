from django.urls import path

from orders.views import OrderCreateView, SuccessTemplateView, CancelTemplateView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('success/', SuccessTemplateView.as_view(), name='success'),
    path('cancel/', CancelTemplateView.as_view(), name='cancel'),
    path('', OrderListView.as_view(), name='orders_list'),
]
