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

class Battery:
    def battery_info(self):
        return 'It has a good battery'
    
class Engine:
    def engine_info(self):
        return 'It has an engine'

class ElectricCarTwo(Car, Battery, Engine):
    pass

my_new_tesla = ElectricCarTwo('a', 'b')
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())