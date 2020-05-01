from rest_framework import serializers

from .models import State, UOM, GSTSlab


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class GSTSlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSTSlab
        fields = '__all__'


class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'
