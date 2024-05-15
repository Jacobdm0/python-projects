#Daniel Mann
#CSE111 
#week 2 checkpoint: calling functions

import math

#Function to calulate and return number of boxes needed
def box_calc(items, box):
    box_num=math.ceil(items/box)
    print(f"If you have {items} items, with {box} in each box, you will need {box_num} boxes.")


#user input variables for number of items
num_items=int(input("Enter the number of items: "))
#input variable for the number of items to be packed in each box
items_box =int(input("Enter the number of items per box: "))
#calls the calulation function
box_calc(num_items,items_box) 

