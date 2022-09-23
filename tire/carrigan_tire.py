from tire.tire import tire


class CarriganTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        service_needed = False
        for number in sensor_array:
            if number >= 0.9 service_needed = True
        return service_needed
