# serializers.py
from rest_framework import serializers
from .models import PiesDev

class PiesDevSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiesDev
        fields = ['part_number', 'part_type_name', 'brand_owner_name', 'brand_name','sub_brand_name']