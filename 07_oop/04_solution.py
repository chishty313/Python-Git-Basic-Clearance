class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.model} {self.__brand}"
    
    def get_brand(self):
        return self.__brand + ' !'

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar('Tesla', 'Model S', '85kWh')
print(my_tesla.model)
print(my_tesla.get_brand())
print(my_tesla.battery_size)
print(my_tesla.fullname())