""" 
Daniel Mann
team teach week 2
sale calulation 
"""
"""
Date time codes
0- Monday
1- Tuesday
2- Wednesday
3- Thursday
4- Friday
5- Saturday
6- Sunday
"""
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
#current_date_and_time = datetime.now()
current_date_and_time=4
print(current_date_and_time)

#calculates the customers price
subtotal=0
item_price=1
while item_price != 0:
    item_price=int(input("how much did the item cost? "))
    item_quant=int(input("how many did you buy? "))
    subtotal+=(item_price*item_quant)
print(subtotal)
#takes the total that the customer spent and checkes agaist the date to find the price before sales tax
if subtotal >= 50:      
    if current_date_and_time == 1 or current_date_and_time == 2:
        discount= round(subtotal*0.1,2)
        pre_tax = subtotal-discount
        print(f"Discount amount: ${discount}")
    else:
        pre_tax=subtotal
elif subtotal<50:
    missing_cost=50-subtotal
    print(f"If you had spent {missing_cost} more, you would have received a 10% discount")
    pre_tax = subtotal

#This calculates the price and the sales tax
sales_tax = round(pre_tax*0.06,2)
final_price= round(pre_tax + sales_tax,2)

#Returns the sales tax and final price to the customer
print(f"Sales tax amount: ${sales_tax}")
print(f"Your final price is: ${final_price}")



