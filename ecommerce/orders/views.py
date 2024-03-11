from rest_framework import generics
from orders.models import Order
from orders.serializers import OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        products = self.request.query_params.get('products')
        customer = self.request.query_params.get('customer')

        if products:
            products_list = products.split(',')
            queryset = queryset.filter(order_items__product__name__in=products_list).distinct()

        if customer:
            queryset = queryset.filter(customer__name=customer)

        return queryset

class OrderRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
