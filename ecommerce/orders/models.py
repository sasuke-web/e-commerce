from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.order_number

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.all().order_by('id').last()
            if not last_order:
                self.order_number = 'ORD00001'
            else:
                order_number = int(last_order.order_number[3:]) + 1
                self.order_number = f'ORD{order_number:05}'
        super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order: {self.order.order_number})"
