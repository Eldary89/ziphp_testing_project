from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.db.models import FloatField, Value, F
from django.db.models.functions import Log

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneModelViewSet(ModelViewSet):
    """
    API to work with airplanes. All airplanes have uuid as unique identifier
    Use GET method to get all airplanes with calculated fuel consumptions and total flight time.
    Use POST method to create new airplane with type id and passengers assumptions
    Use PUT and PATCH to modify existed airplane
    USE DELETE to delete the airplane
    """

    serializer_class = AirplaneSerializer

    def get_queryset(self):
        return Airplane.objects.annotate(
            fuel_consumption_per_minute=Value(Airplane.FUEL_CONSUMPTION_MULTIPLIER) * Log(2, F('type_id')) \
                + Value(Airplane.PASSENGER_FUEL_CONSUMPTION_MULTIPLIER) * F('passenger_assumption'),
            total_flight_time=Value(Airplane.LITRE_CAPACITY_MULTIPLIER) * F('type_id') \
                / F('fuel_consumption_per_minute')
        ).all()
