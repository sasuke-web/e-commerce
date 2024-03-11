from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'weight']

    def validate_name(self, value):
        if self.instance and self.instance.name == value:
            return value
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("A product with this name already exists.")
        return value

    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError("Weight must be a positive decimal and not more than 25.")
        return value
