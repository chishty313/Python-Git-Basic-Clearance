class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def fullname(self):
        return f"{self.__model} {self.__brand}"
    
    def get_brand(self):
        return self.__brand + ' !'
    
    def fuel_type(self):
        return 'Petrol or diesel'
    
    @staticmethod
    def general_description():
        return 'Cars are means of transport'
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric Charge'

my_car = Car('Toyota', 'Corolla')
print(my_car.model)