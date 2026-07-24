# Parent Class
class TrafficDevice:
    def activate(self):
        pass

# Child Classes
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic Light: Changing sequence to GREEN.")

class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed Camera: Activating radar to monitor speeds.")

class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian Signal: Beeping and displaying 'WALK' sign.")

class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency Siren: Sounding alarm to clear the intersection!")

# Create one object of each class and store them in a list
traffic_devices = [
TrafficLight(),
SpeedCamera(),
PedestrianSignal(),
EmergencySiren()
]

# Activate them without checking their types in a loop
for device in traffic_devices:
    device.activate()