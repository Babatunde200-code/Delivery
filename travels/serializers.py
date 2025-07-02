from rest_framework import serializers
from .models import TravelPlan

class TravelPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPlan
        fields = ['id', 'origin_country', 'destination_country', 'departure_date']
