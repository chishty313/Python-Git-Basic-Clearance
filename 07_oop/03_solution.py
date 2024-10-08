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
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_size)
print(my_tesla.fullname())

my_car = Car('Toyota', 'Corolla')
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())

my_new_car = Car('Tata', 'Safari')
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.fullname())