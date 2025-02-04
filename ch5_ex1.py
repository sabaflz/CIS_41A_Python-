# CIS 41A
# Ch.5, Ex.1
# Saba Feilizadeh
# Write three functions to:
# - Get the hours and rate from the user
# - Validate the inputs
# - Calculate the  gross pay (account for overtime pay)
# - Implement the following functions:
#   get_input, compute_pay, print_output


# A constant for the overtime hour limit
OVERTIME = 40
# Overtime rate factor
OVERTIME_FACTOR = 1.5
# Constant for the floating point precision
PRECISION = 2
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
    Gets valid numeric input from the user.

    Args: -

    Returns:
        hours, rate: The values of hours and rate.
    """

    # Try to get valid inputs from the user
    valid_hour = False
    while not valid_hour:
        # Get valid inputs (hours and rate)
        hours = validate_input("Enter Hours: ")

        if hours is not None:   # means we have a valid input for hours

            valid_rate = False
            while not valid_rate:
            
                rate = validate_input("Enter Rate: ")

                if rate is not None: # means we have a valid input for rate
                    valid_rate = True

            valid_hour = True  

    return hours, rate

# --------------------------------------------------------------------------
def compute_pay(hours, rate):
    """
    Computes the total pay (including the overtime).

    Args:
        hours, rate: The validated amount for hours and rate.
    
    Returns:
        pay: The total pay (including the overtime).
    """

    # Calculate pay
    pay = hours * rate

    # Overtime condition (the rate would be 50% more)
    if hours > OVERTIME:
        pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)
    
    return pay

# --------------------------------------------------------------------------
def print_output(pay):
    """
    Prints the total pay.

    Args:
        pay: The total pay.

    Returns: -
    """
    # Output for the user
    print("Your gross pay is", round(pay , PRECISION), "dollars.")
    
# --------------------------------------------------------------------------
def main():
    
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)
    
# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------   


'''
Outputs:

Enter Hours: 42
Enter Rate: 17.25
Your gross pay is 741.75 dollars.
Done!

---------------------------------------------------

Enter Hours: fifty
Error, please enter a numeric input!
Enter Hours: -12
Please enter positive numbers!
Enter Hours: 23.333
Enter Rate: five
Error, please enter a numeric input!
Enter Rate: -17
Please enter positive numbers!
Enter Rate: 19.777
Your gross pay is 461.46 dollars.
Done!

'''
