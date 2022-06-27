from rest_framework.serializers import ModelSerializer, FloatField
from .models import Airplane


class AirplaneSerializer(ModelSerializer):
    fuel_consumption_per_minute = FloatField(read_only=True)
    total_flight_time = FloatField(read_only=True)

    class Meta:
        model = Airplane
        fields = (
            'uuid',
            'type_id',
            'passenger_assumption',
            'fuel_consumption_per_minute',
            'total_flight_time',
        )

