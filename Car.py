class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70


    def drive(self, kilometraj):
        if (self.fuel - kilometraj/10) >= 0:
            self.__add_distance(kilometraj)
            self.__subtract_fuel(kilometraj)
            print("let\'s drive")
        else:
            print("need more fuel, please, fill more!")
        
    def __add_distance(self, kilometraj):
            self.odometer += kilometraj    


    def __subtract_fuel(self, kilometraj):
        self.fuel -= kilometraj/10

car = Car('BMW', 'B5', '2015')
print(car.make, car.model, car.year)
car.drive(1000)
print(car.odometer)
print(car.fuel)
    

        


