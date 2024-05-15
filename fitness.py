# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
def main():
    # Get the user's gender, birthdate, height, and weight.
    gender=input("what is your gender? M/F ")
    birthdate=input("what is your birthdate? (YYYY-MM-DD) ")
    weight_lbs=float(input("what is your weight in pounds? "))
    height_imperial_ft=int(input("how may feet tall are you? "))
    height_imperial_in=int(input("how many inches tall are you? "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    height_inchs=inch_conversion(height_imperial_ft,height_imperial_in)
    age=compute_age(birthdate)
    weight_kg=kg_from_lb(weight_lbs)
    height_cm=cm_from_in(height_inchs)
    bmi=body_mass_index(weight_kg, height_cm)
    bmr= basal_metabolic_rate(gender, weight_kg, height_cm, age)
    # Print the results for the user to see.
    if isinstance(bmr, int)==True:
        print(f"Age: {age} years")
        print(f"Weight: {weight_kg} kilograms")
        print(f"Height: {height_cm/100} meters")
        print(f"Body mass index: {bmi}")
        print(f"Basal metabolic rate (kcal/day): {bmr}")
    else:
        print(bmr)


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()


    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def inch_conversion(feet,inchs):
    """
    Convert a person's height in feet and inches to just inches
        parameter feet: a person's height in feet
        parameter inchs: a person's height in inches
        return: a person's height in inches
    """
    inch_height= (feet*12) + inchs
    return inch_height
def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight_KG= round(pounds*0.45359237,2)

    return weight_KG


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height_cm= round(inches*2.54,1)
    return height_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    
    """
    bmi= round(10000*weight/(height**2),1)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    (women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
    (men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
    """
    if gender.lower()=="m":
       bmr=int(88.362 + (13.397*weight) + (4.799*height) - (5.677*age)) 
    elif gender.lower()=="f":
       bmr= int(447.593 + (9.247*weight) + (3.098*height) - (4.330*age))
    else:
        bmr="invalid gender, unable to proceed"
    return bmr
   
    


# Call the main function so that
# this program will start executing.
main()