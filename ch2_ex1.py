# CIS 41A
# Ch.2, Ex.1
# Saba Feilizadeh
# Compute gross pay using hours and rate per hour

# Constant for the floating point precision
PRECISION = 2

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate
print("Pay: ", round(pay, PRECISION))


'''
Outputs:

Enter Hours: 37
Enter Rate: 24.25
Pay:  897.25

------------------

Enter Hours: 12
Enter Rate: 17.25
Pay:  207.0

'''
