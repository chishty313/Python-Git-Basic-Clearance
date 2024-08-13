class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.model} {self.brand}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar('Tesla', 'Model S', '85kWh')
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))