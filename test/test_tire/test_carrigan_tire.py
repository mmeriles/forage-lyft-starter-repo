import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0, 0.95, 0.8, 0.1]
        tire = CarriganTire(sensor_array)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        sensor_array = [0, 0.7, 0.8, 0.1]
        tire = CarriganTire(sensor_array)
        self.assertFlase(battery.needs_service())
