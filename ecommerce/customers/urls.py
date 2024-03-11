from django.urls import path
from customers.views import CustomerRetrieveUpdateAPIView, CustomerListCreateAPIView

urlpatterns = [
    path('', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('<int:pk>/', CustomerRetrieveUpdateAPIView.as_view(), name='customer-retrieve-update'),
]
