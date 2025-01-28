# CIS 41A
# Ch.4, Ex.2
# Saba Feilizadeh
# Calculate the total pay with overtime rate of 1.5
# if the hours is greater than 40 per week
# Handle the non-numeric inputs
# Keep asking the user to enter input

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

    # Get company name from the user (no NOT validate)
    company_name = input("Enter your company name: ").strip()

    valid_hour = False

    while not valid_hour:
        # Get valid inputs (hours and rate)
        hours = get_float_input("Enter Hours: ")

        if hours is not None:   # means we have a valid input for hours

            valid_rate = False

            while not valid_rate:
            
                rate = get_float_input("Enter Rate: ")

                if rate is not None: # means we have a valid input for rate

                    # Calculate pay
                    pay = hours * rate
                    
                    # Overtime condition (the rate would be 50% more)
                    if hours > OVERTIME:
                        pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)
                    
                    # Output
                    print("\n\nCompany: ", company_name)
                    print("Hours: ", round(hours , PRECISION))
                    print("Rate: ", round(rate , PRECISION))
                    print("\n" + "*" * STAR_NUM + "\n")
                    # A random number between LOWER_BOUND to UPPER_BOUND for document numbers
                    print("Your document number is: ", randint(LOWER_BOUND, UPPER_BOUND))
                    print("Your", company_name, "gross pay is", round(pay, PRECISION), "dollars.")

                    valid_rate = True

            valid_hour = True

# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------


'''
Outputs:

Enter your company name:  Google
Enter Hours: 42
Enter Rate: 17.25


Company:  Google
Hours:  42.0
Rate:  17.25

******************************

Your document number is:  1934
Your Google gross pay is 741.75 dollars.
Done!

---------------------------------------------------

Enter your company name: Apple
Enter Hours: fifty
Error, please enter a numeric input!
Enter Hours: -17
Please enter positive numbers!
Enter Hours: 23.333
Enter Rate: seven
Error, please enter a numeric input!
Enter Rate: -9
Please enter positive numbers!
Enter Rate: 19.777


Company:  Apple
Hours:  23.33
Rate:  19.78

******************************

Your document number is:  1283
Your Apple gross pay is 461.46 dollars.
Done!

---------------------------------------------------

Enter your company name:        Microsoft
Enter Hours:    16
Enter Rate:               23.456


Company:  Microsoft
Hours:  16.0
Rate:  23.46

******************************

Your document number is:  1082
Your Microsoft gross pay is 375.3 dollars.
Done!

'''
