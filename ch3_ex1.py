# CIS 41A
# Ch.3, Ex.1
# Saba Feilizadeh
# Calculate the overtime (if the hours is greater than 40 per week
# Overtime rate 1.5)

# A constant for the overtime hour limit
OVERTIME = 40

# Overtime rate factor
OVERTIME_FACTOR = 1.5

# Constant for the floating point precision
PRECISION = 2

# Get input from user
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Calculate pay
pay = hours * rate

# Overtime condition (the rate would be 50% more)
if hours > OVERTIME:
    pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)


print("Pay: ", round(pay, PRECISION))

print("Done!")


'''
Outputs:

Enter Hours: 37
Enter Rate: 24.25
Pay:  897.25
Done!

------------------

Enter Hours: 42
Enter Rate: 17.25
Pay:  741.75
Done!

'''
