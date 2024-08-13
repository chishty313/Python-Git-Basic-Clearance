class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    
    def fullname(self):
        return f"{self.model} {self.__brand}"
    
    def get_brand(self):
        return self.__brand + ' !'
    
    def fuel_type(self):
        return 'Petrol or diesel'

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric Charge'

ElectricCar('Tesla', 'Model S', '85kWh')
Car('Tata', 'Safari')
Car('Tata', 'Nexon')

print(Car.total_car)