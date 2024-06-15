from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

entry_sensor = EntrySensor(id=1, car_park=car_park, is_active=True)
exit_sensor = ExitSensor(id=2, car_park=car_park, is_active=True)
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

car_park.write_config()

# 10 cars in
for _ in range(10):
    entry_sensor.detect_vehicle()
# 2 cars out
for _ in range(2):
    exit_sensor.detect_vehicle()

# Print the state of the car park and the display
print(car_park)
print(display)

print(f"Log file was updated: {car_park.log_file}")
