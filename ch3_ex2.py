# CIS 41A
# Ch.3, Ex.2
# Saba Feilizadeh
# Calculate the total pay with overtime rate of 1.5
# if the hours is greater than 40 per week
# Handle the non-numeric inputs

# Overtime hour limit
OVERTIME = 40

# Overtime rate factor
OVERTIME_FACTOR = 1.5

# Floating point precision
PRECISION = 2

# ------------------------------------------------------
# Validate user inputs
def get_float_input(prompt):
    """
    Gets and validates numeric input from the user.

    Args:
        prompt (str): The message to display when requesting user input.

    Returns:
        float or None: The validated float value if successful,
                       None if validation fails.
    """

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
# ------------------------------------------------------
def main():
    # Get input values
    hours = get_float_input("Enter Hours: ")

    if hours is not None:   # means we have a valid input for hours

        rate = get_float_input("Enter Rate: ")

        if rate is not None: # means we have a valid input for rate

            # Calculate pay
            pay = hours * rate
            
            # Overtime condition (the rate would be 50% more)
            if hours > OVERTIME:
                pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)
                
            print("Pay: ", pay)

# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------

'''
Outputs:

Enter Hours: 42
Enter Rate: 17.25
Pay:  741.75
Done!

------------------

Enter Hours: 23
Enter Rate: five
Error, please enter a numeric input!
Done!

------------------

Enter Hours: fifty
Error, please enter a numeric input!
Done!

------------------

Enter Hours: -17
Please enter positive numbers!
Done!

'''
