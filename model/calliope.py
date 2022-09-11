from abc import ABC

from car import Car

from engine import CapuletEngine
from battery import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self, engine, battery):
        if engine.needs_service or battery.needs_service return True
        else return False
