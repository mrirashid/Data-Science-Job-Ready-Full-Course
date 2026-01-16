## Explain why self is used in python OOP
class Car:
    speed=0
    def drive(self):
        self.speed=100
my_car=Car()
my_car.drive()
print(my_car.speed) 