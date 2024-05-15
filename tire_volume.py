#Daniel Mann
#cse 111 week 2, prove assignment
"""
This program is meant to calculate the volume of a tire based on inputs from the user
and then
"""

#gets the needed variables from the user
tire_width = float(input("Please enter the tire width in mm:"))
tire_ratio = float(input("Please enter the tire's aspect ratio:"))
tire_dia = float(input("Please enter the tire's diameter in inches:"))

# calculated the volume of the tire using this formula
#v = πw^2a(wa + 2,540d)/10,000,000,000 
#with w as width, a as the ratio, and d as the diameter

import math
tire_volume =round( (math.pi*(tire_width*tire_width)*tire_ratio*(tire_width*tire_ratio + 2540*tire_dia)) /10000000000, 2)
print(f"The aproximate volume of the tire is {tire_volume} liters.")

# Import the datetime class from the datetime.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date = datetime.now()
# asks the user if they want to buy tires that match what they entered
tire_buy=input("would you like to buy tires with those dimmensions? Y/N ")
#if they wanted to buy the tires, this will store their contact info so they can get the tires
if tire_buy.lower=='y':
    phone_num=input("what is you phone number? ")
    data=open("volumes.txt",mode="at")
    print(f"Time: {current_date:%Y-%m-%d}, Tire Width: {tire_width}, Aspect Ratio: {tire_ratio}, Diameter: {tire_dia}, Volume:{tire_volume}", file=data)
    print(f"Phone: {phone_num}")
    data.close()
else:
    # if they didnt want to buy the tires, 
    # the measuments they wanted are still stored so that they 
    # can be anayzed later to see to what kind of tires are most wanted
    data=open("volumes.txt",mode="at")
    print(f"Time: {current_date:%Y-%m-%d}, Tire Width: {tire_width}, Aspect Ratio: {tire_ratio}, Diameter: {tire_dia}, Volume:{tire_volume}", file=data)
    data.close()


