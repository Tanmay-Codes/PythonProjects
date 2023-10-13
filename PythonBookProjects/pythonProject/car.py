class Battery:
    def __init__(self):
        self.power = 1500

    def describe_battery(self):
        print(f"The battery is of {self.power} mAh")


class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.milage = 0
        self.battery = Battery()
        print(f"I have a {self.name}, {self.year} and I love it")

    def odometer(self, speed):
        if speed > 70:
            self.milage = 100
            print(f"The milage of my car is {self.milage} if speed is {speed} km")
        else:
            self.milage = 200
            print(f"The milage of my car is {self.milage} if speed is {speed} km")


