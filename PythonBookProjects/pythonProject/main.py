# from user import User
#
# user_files = User()
# response = True
#
# while response:
#     user_files.store()
#     choice = input("Do you want to enter more? Y/N: ").lower()
#     if choice == 'n':
#         response = False
#
# print("Enter your login details")
# name = input("User name: ")
# password = input("Password: ")
# user_files.search(name, password)
#

from car import Car

my_car = Car("Tesla model-S", "2009")
my_car.odometer(50)
my_car.battery.describe_battery()