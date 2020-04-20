# public => memberName
# protected => _memberName
# private => __memberName

class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017 #

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)

car = Car()
print("Print attribute numberOfWheels: ", car.numberOfWheels)
bmw = Bmw()
# if we use (car.__yearOfManufacture), it will be an error because
# it saves 2017 inside Car class as _Car__yearOfManufacture
print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)