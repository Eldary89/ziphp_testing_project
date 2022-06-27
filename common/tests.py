from django.test import TestCase
from rest_framework.test import APIClient
from .models import Airplane

from math import log


class CreateAndGetAirplaneTestCase(TestCase):
    """
    TestCase to check if creation and retrieving of airplane data works correct
    """
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_airplanes(self):
        for id, passenger_assumption in zip(range(1, 11), range(50, 201, 15)):
            create_response = self.client.post(
                '/api/v1/common/airplane/',
                data={
                    "type_id": id,
                    "passenger_assumption": passenger_assumption
                }
            )
            self.assertEqual(create_response.status_code, 201)
        get_response = self.client.get('/api/v1/common/airplane/')
        self.assertEqual(len(get_response.data), 10)


class CorrectCalculationAirplaneTestCase(TestCase):
    """
    TestCase to check if creation and retrieved calculated data is correct
    """
    def setUp(self) -> None:
        airplanes = Airplane.objects.bulk_create([
            Airplane(
                type_id=id,
                passenger_assumption=passenger_assumption
            )
            for id, passenger_assumption in zip(range(1, 11), range(50, 201, 15))
        ])
        self.client = APIClient()

    def test_correct_calculations(self):
        airplanes = list(sorted(self.client.get('/api/v1/common/airplane/').data, key=lambda x: x['type_id']))
        for id, passenger_assumption, airplane in zip(range(1, 11), range(50, 201, 15), airplanes):
            fuel_consumption = Airplane.FUEL_CONSUMPTION_MULTIPLIER * log(id, 2) + \
                Airplane.PASSENGER_FUEL_CONSUMPTION_MULTIPLIER * passenger_assumption
            self.assertEqual(fuel_consumption, airplane['fuel_consumption_per_minute'])
            self.assertEqual(
                Airplane.LITRE_CAPACITY_MULTIPLIER * id / fuel_consumption, airplane['total_flight_time']
            )


