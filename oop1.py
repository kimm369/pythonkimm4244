class Fuits:
    def __init__(self, name, price):
       self.name=name
       self.price=price
    def onyesha(self):
      print(f"This fruit is {self.name} and the price is {self.price}")
myobj=Fuits("mango", 30)
myobj.onyesha()