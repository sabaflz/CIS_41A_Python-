# CIS 41A
# Ch.5, Ex.2
# Saba Feilizadeh
# Write three functions to:
# - Get the hours and rate from the user
# - Validate the inputs
# - Calculate the  gross pay (account for overtime pay)
# - Implement the following functions:
#   get_input, compute_pay, print_output
# - Ask for company name and include it in the output
# - Print a random number between 1000 to 2000 for document numbers.

from random import randint

# A constant for the overtime hour limit
OVERTIME = 40
# Overtime rate factor
OVERTIME_FACTOR = 1.5
# Constant for the floating point precision
PRECISION = 2

# Number of stars used in the output
STAR_NUM = 30
# The boundries for choosing the random number
LOWER_BOUND = 1000
UPPER_BOUND = 2000
# --------------------------------------------------------------------------
def validate_input(prompt):
    """
    Gets and validates numeric input from the user.

    Args:
        prompt (str): The message to display when requesting user input.

    Returns:
        float or None: The validated float value if successful,
                       None if validation fails.
    """

    flag = True
    while flag:
        try:
            value = float(input(prompt))

            # Handle negative inputs
            if value < 0:
                print("Please enter positive numbers!")
                return None
            return value
        
        # Handle non-numeric inputs
        except ValueError:
            print(f"Error, please enter a numeric input!")
            return None
# --------------------------------------------------------------------------
def get_input():
    """
    Gets valid numeric inputs from the user (company_name, hours, and rate).

    Args: -

    Returns:
        company_name (str): User's comapny name (No extra spaces using strip()).
        hours, rate (float): The values of hours and rate.
    """

    # Get user's company name
    company_name = input("Enter your company name: ").strip()

    # Try to get valid inputs from the user
    valid_hour = False
    while not valid_hour:
        # Get valid inputs (hours and rate)
        hours = validate_input("Enter the hours: ")

        if hours is not None:   # means we have a valid input for hours

            valid_rate = False
            while not valid_rate:
            
                rate = validate_input("Enter the rate: ")

                if rate is not None: # means we have a valid input for rate
                    valid_rate = True

            valid_hour = True  

    return company_name, hours, rate

# --------------------------------------------------------------------------
def compute_pay(hours, rate):
    """
    Computes the total pay (including the overtime).

    Args:
        hours, rate (float): The validated amount for hours and rate.
    
    Returns:
        pay (float): The total pay (including the overtime).
    """

    # Calculate pay
    pay = hours * rate

    # Overtime condition (the rate would be 50% more)
    if hours > OVERTIME:
        pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)
    
    return pay

# --------------------------------------------------------------------------
def print_output(company_name, hours, rate, pay):
    """
    Prints a random number as user's document number,the company name,
    and total pay.

    Args:
        company_name (str): Name of user's company.
        hours, rate (float): The validated amount for hours and rate.
        pay (float): The total pay.

    Returns: -
    """
    # Output for the user
    print()
    print("Company:", company_name)
    print("Hours:", hours)
    print("Rate:", rate)
    print("*" * STAR_NUM)
    print("Your document number is:", randint(LOWER_BOUND, UPPER_BOUND))
    print(f"Your {company_name} gross pay is", round(pay , PRECISION), "dollars.")
    
# --------------------------------------------------------------------------
def main():
    
    the_company_name, the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_company_name, the_hours, the_rate, the_pay)
    
# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------   

'''
Outputs:

Enter your company name:      Google
Enter the hours: 42
Enter the rate: 17.25

Company: Google
Hours: 42.0
Rate: 17.25
******************************
Your document number is: 1352
Your Google gross pay is 741.75 dollars.
Done!

---------------------------------------------------

Enter your company name: Apple
Enter the hours: fifty
Error, please enter a numeric input!
Enter the hours: -36
Please enter positive numbers!
Enter the hours: 23.333
Enter the rate: five
Error, please enter a numeric input!
Enter the rate: -9
Please enter positive numbers!
Enter the rate: 19.777

Company: Apple
Hours: 23.333
Rate: 19.777
******************************
Your document number is: 1133
Your Apple gross pay is 461.46 dollars.
Done!

---------------------------------------------------

Enter your company name:         Microsoft
Enter the hours:      16
Enter the rate:       23.456

Company: Microsoft
Hours: 16.0
Rate: 23.456
******************************
Your document number is: 1802
Your Microsoft gross pay is 375.3 dollars.
Done!

'''