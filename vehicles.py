# 1. Define 5 of your favorite vehicles
# 2. Move all common properties in your vehicles to a new Vehicle class.
# 3. Create an instance of each vehicle.
# 4. Define a different value for each vehicle's properties.
# 5. Create a drive() method in the Vehicle class.
# 6. Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# 7. Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# 8. Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# 9. Make your vehicle instances perform all three behaviors.

class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""

     def drive(self):
            print("Vroooom!")

class Jeep(Vehicle):
    def __init__(self):
        self.can_remove_top = False

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

class Ram(Vehicle):
    class Ram:
        def __init__(self):
        self.fuel_capacity = 0