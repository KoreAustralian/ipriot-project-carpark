from sensor import Sensor
from display import Display
from pathlib import Path


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = Path(log_file) if log_file else Path("log.txt")

    @property
    def available_bays(self):
        # car_park.available_bays
        return max(0, self.capacity - len(self.plates))

    def __str__(self):
        return f'Welcome to {self.location} car park'

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
        self.write_log(f"Car added: {plate}")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.write_log(f"Car removed: {plate}")

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42})
            print(f"Updating: {display}")

    def write_log(self, event):
        with self.log_file.open("a") as log:
            log.write(event + "\n")
