from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=11, trigger=12)
while True:
    print(ultrasonic.distance)