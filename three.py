class Car:
    def __init__(self, name, price):
        self.carname = name
        self.carprice = price

    def pricediff(self, cartwo):
        diff = self.carprice - cartwo.carprice
        return diff
    
    def __str__(self):
        return "The name of the car is " + str(self.carname)
    
    def __add__(self, other):
       return self.carprice + other.carprice
    
    def __eq__(self, other):
        return self.carprice == other.carprice
        
    def usedCar(self):
        price = self.carprice / 2
        name = self.name
        return Car(name, price)
        
car = Car("Honda CRV", 56000)
cartwo = Car("Toyota", 52000)

p = car.pricediff(cartwo) # p = Car.pricediff(car, cartwo)
print("Price difference is: ${} CAD.".format(p))

print(car + cartwo)
print(car == cartwo)