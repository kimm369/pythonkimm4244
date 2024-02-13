class Car:
    def __init__(self,make,model,year, color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def onyesha (self):
        print(f"My dream car is {self.make} and my model is {self.model} manufactured in {self.year} the color is {self.color}")
myobj=Car("Toyota","Vits",2020, "red")
myobj.onyesha()
myobj2=Car("BMW", "Sports", 2022, "brown")
myobj2.onyesha()