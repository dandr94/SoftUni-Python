from project.car import Car

class SportsCar(Car):
    def race(self):
        return 'racing...'


sports_car = SportsCar()
print(sports_car.move())
print(sports_car.drive())
print(sports_car.race())