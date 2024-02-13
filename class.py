class Gari:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def describe_gari(self):
        return f"{self.model} {self.year} {self.make}"
    def read_odometer(self):
        return f"{self.model} {self.year} {self.make}"

    def update_odometer(self,milage):
        if milage>= self.odometer_reading:
            self.odometer_reading=milage
        else:
            print("You cant roll back an odometer")
    def increment_odometer(self, miles):
        self.odometer_reading+=miles
my_car=Gari("Toyota", "Vits", 2020)

print(my_car.describe_gari())
print(my_car.read_odometer())
my_car.update_odometer(100)
print(my_car.read_odometer())
my_car.increment_odometer(50)
print(my_car.read_odometer)