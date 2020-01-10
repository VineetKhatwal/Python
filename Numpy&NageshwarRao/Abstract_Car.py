from abc import *

class Car:

    def __init__(self, regNo):
        self.regNo = regNo

    def openTank(self):
        print("Filing fuel to car", self.regNo)

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass

class Maruti(Car):

    def steering(self):
        print("Manual Steering")

    def braking(self):
        print("Hydraulic brake")

class Hyundai(Car):

    def steering(self):
        print("Power Steering")

    def braking(self):
        print("Gas brake")

print("------------------ MARUTI -----------------")

m = Maruti("UK04 R 7755")
m.openTank()
m.steering()
m.braking()

print("----------------- HYUNDAI -----------------")

s = Hyundai("UK04 R 7755")
s.openTank()
s.steering()
s.braking()
