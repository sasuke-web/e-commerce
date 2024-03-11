from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('<int:pk>/', views.OrderRetrieveUpdateAPIView.as_view(), name='order-retrieve-update'),
]
