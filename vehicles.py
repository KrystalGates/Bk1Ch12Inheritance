# 1. Define 5 of your favorite vehicles
# 2. Move all common properties in your vehicles to a new Vehicle class.

class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
        print(f'Turns to the {direction}')

    def stop(self):
        print(f'Vehicle comes to a stop')

class Jeep(Vehicle):
    def __init__(self):
        self.can_remove_top = False
        self.fuel_capacity = 0

    def drive(self):
        print(f'The {self.main_color} Jeep drives by. RUMMM')

    def turn(self,direction):
        print(f'The jeep turns to the {direction} over a rock')

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print(f'The {self.main_color} Tesla drives by. WOOOOO')

    def stop(self):
        print(f'The telse quietly comes to a stop')

class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def drive(self):
        print(f'The {self.main_color} Ram Drives past. RUUUUMMM')

    def stop(self):
        print(f'The truck rolls to a hard stop')

    def turn(self,direction):
        print(f'The truck turns hard to the {direction}')
# 3. Create an instance of each vehicle.
wrangler = Jeep()
s10 = Tesla()
truck = Ram()

# 4. Define a different value for each vehicle's properties.
wrangler.main_color = "green"
wrangler.maximum_occupancy = 5
wrangler.can_remove_top =True
wrangler.fuel_capacity = 14

s10.main_color = "white"
s10.maximum_occupancy = 5
s10.battery_kwh =62

truck.main_color = "black"
truck.maximum_occupancy = 3
truck.fuel_capacity = 18


# 5. Create a drive() method in the Vehicle class.
# 6. Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# 7. Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# 8. Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# 9. Make your vehicle instances perform all three behaviors.

wrangler.drive()
wrangler.stop()
wrangler.turn("right")

s10.drive()
s10.stop()
s10.turn("left")

truck.drive()
truck.stop()
truck.turn("left")
