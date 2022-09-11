from abc import ABC

from car import Car

from engine import SternmanEngine
from battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self, engine, battery):
        if engine.needs_service or battery.needs_service return True
        else return False
