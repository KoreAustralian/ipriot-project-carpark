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