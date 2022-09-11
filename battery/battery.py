from abc import ABC, abstractmethod

from car import Car

class Battery(Car, ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service(self):
        pass
