import unittest
from datetime import datetime


class TestCarFactory(unittest.TestCase):

# battery and the engine both need service
# battery needs service, but the engine doesn't
# engine needs service, but battery doesn't
# neither the battery nor the engine need service
# if there is a new feature, we need new tests, but I think it'll be okay like this?


class TestCalliope(unittest.TestCase):
    def test_both_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 40000
        last_service_mileage = 0
    
        car= create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        sef.assertTrue(car.needs_service())
        
    def test_only_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car= create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_only_engine_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 40000
        last_service_mileage = 0

        car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_neither_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_both_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 70000
        last_service_mileage = 0
    
        car= create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        sef.assertTrue(car.needs_service())
        
    def test_only_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car= create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_only_engine_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 70000
        last_service_mileage = 0

        car = create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_neither_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_both_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = True
    
        car= create_palindrome(current_date, last_service_date, warning_light_is_on)
        sef.assertTrue(car.needs_service())
        
    def test_only_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car= create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_only_engine_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = True

        car = create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_neither_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_both_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 70000
        last_service_mileage = 0
    
        car= create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        sef.assertTrue(car.needs_service())
        
    def test_only_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car= create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_only_engine_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 70000
        last_service_mileage = 0

        car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_neither_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_both_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 40000
        last_service_mileage = 0
    
        car= create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        sef.assertTrue(car.needs_service())
        
    def test_only_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car= create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_only_engine_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 40000
        last_service_mileage = 0

        car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_neither_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
