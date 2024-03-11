from django.urls import path
from orders.views import OrderListCreateAPIView, OrderRetrieveUpdateAPIView

urlpatterns = [
    path('', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='order-retrieve-update'),
]
