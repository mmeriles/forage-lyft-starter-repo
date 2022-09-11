from abc import ABC

from car import Car

from engine import WilloughbyEngine
from battery import NubbinBattery


class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self, engine, battery):
        if engine.needs_service or battery.needs_service return True
        else return False
