import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0.7, 0.95, 0.9, 0.8]
        tire = OctoprimeTire(sensor_array)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        sensor_array = [0, 0, 0, 0]
        tire = OctoprimeTire(sensor_array)
        self.assertFlase(battery.needs_service())
