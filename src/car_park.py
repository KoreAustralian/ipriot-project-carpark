from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self,
                 lacation,
                 capacity,
                 plates = None,
                 sensors = None,
                 displays = None):
        self.lacation = lacation
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Welcome to {self.lacation} car park'

    def register(self, component):
        """Registers components of a car park"""
        if not isinstance(component,  (Sensor, Display)):
            raise TypeError("Invalid component type")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)


    def add_car(self, plate):
        self.plates.append(plate)

    def remove_car(self, plate):
        self.plates.remove(plate)


    def update_displays(self):
        for display in self.displays:
            display.update()
            print(f"Updating: {display}")


