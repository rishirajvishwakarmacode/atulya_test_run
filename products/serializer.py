from rest_framework import serializers
from .models import Product_packed


class ppdtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_packed
        fields = ['id', 'name', 'mrp', 'brand', 'catagory']
