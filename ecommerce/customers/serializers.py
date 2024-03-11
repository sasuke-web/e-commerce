from rest_framework import serializers
from customers.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'contact_number', 'email']
        extra_kwargs = {
            'name': {'validators': []},  # Disable default unique validator
        }

    def validate_name(self, value):
        if self.instance is not None and self.instance.name == value:
            return value
        if Customer.objects.filter(name=value).exists():
            raise serializers.ValidationError("A customer with this name already exists.")
        return value
