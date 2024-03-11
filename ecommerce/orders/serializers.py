from rest_framework import serializers
from django.utils import timezone
from orders.models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer', 'order_date', 'address', 'order_items']

    def validate(self, data):
        # Check cumulative weight
        total_weight = sum(item['product'].weight * item['quantity'] for item in data['order_items'])
        if total_weight > 150:
            raise serializers.ValidationError("The cumulative weight of the order items cannot exceed 150kg.")

        # Check order date
        order_date = data.get('order_date')
        if order_date and order_date < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")

        return data

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
