import unittest
from sensor import EntrySensor
from car_park import CarPark


class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="Test Location", capacity=100)
        self.entry_sensor = EntrySensor(id=1, car_park=self.car_park, is_active=True)

    def test_entry_sensor_initialization(self):
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)
        self.assertTrue(self.entry_sensor.is_active)

    def test_entry_sensor_detect_vehicle(self):
        initial_count = len(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count + 1)
        self.assertTrue(any(plate.startswith("FAKE-") for plate in self.car_park.plates))


if __name__ == "__main__":
    unittest.main()
