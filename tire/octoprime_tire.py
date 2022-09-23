from tire.tire import tire


class OctoprimeTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        sum = 0
        for number in sensor_array:
            sum+= number
        return sum >= 3
