# CIS 41A
# Final - part 1
# Saba Feilizadeh
# A Menu-Driven Program for De Anza College Food Court


# A dictionary for name and prices of the items on the menu
MENU = {
    1: {"name": "De Anza Burger", "price": 5.25},
    2: {"name": "Bacon Cheese", "price": 5.75},
    3: {"name": "Mushroom Swiss", "price": 5.95},
    4: {"name": "Western Burger", "price": 5.95},
    5: {"name": "Con Cali Burger", "price": 5.95}
}

# Constant for tax (staff only)
TAX = 0.09
# Constant for the floating point precision
PRECISION = 2

# Define column widths for the tables in the output
ITEM_WIDTH = 20
GAP = 12
LINE_WIDTH = ITEM_WIDTH + (GAP * 3) + 5

# ------------------------------------------------------
def display_menu():
    """
    Displays the Food Court menu with item numbers, names, and prices.
    
    Args:
        None   
    Returns:
        None     
    Output:
        Prints a formatted menu showing all available items and their prices
    """
    print("-" * LINE_WIDTH)
    print("<<" + "-" * ((LINE_WIDTH - 29) // 2) + " De Anza Food Court Menu " + "-" * ((LINE_WIDTH - 29) // 2)+ ">>\n")
    
    for item_num, details in MENU.items():
        dots = "." * (LINE_WIDTH - len(details["name"]) - len(str(details["price"])) - 7)
        print(f"{item_num}. {details['name']} {dots} $ {details['price']}")
    print("6. Exit")
    print("-" * LINE_WIDTH)

# ------------------------------------------------------
def get_inputs():
    
    """
    Gets the user's order and status (student/staff).
    
    Args:
        None    
    Returns:
        tuple: Contains two elements:
            - order (dict): Dictionary with item numbers as keys and quantities as values
            - status (int): User's status code where:
                * -1: No order placed
                * 0: Student
                * 1: Staff          
    Output:
        Prints prompts for user input and validation messages
    """

    # Initialize order dictionary with zero quantities
    order = {item_num: 0 for item_num in MENU.keys()}
    wants_to_order = False

    # Get and validate user's order
    status = -1
    keep_ordering = True
    while keep_ordering:
        try:
            user_choice = int(input("What would you like to order?\n(Enter a number between 1 to 5 to select your order or enter 6 to exit):  "))
            # Check if user wants to exit without ordering
            if user_choice == 6:
                if not wants_to_order:
                    print("\nThank you, hope to see you again!")
                # Exit the menu
                keep_ordering = False
            
            elif user_choice in MENU:
                wants_to_order = True
                # Get how many of the selected burger the user wants
                valid_input = False
                while not valid_input:
                    try:
                        item_quantity = int(input(f"How many of {MENU[user_choice]['name']} would you like to order? "))
                        if item_quantity <= 0:
                            print("Please enter a positive number!")
                        else:
                            order[user_choice] += item_quantity
                            valid_input = True

                    except ValueError:
                        print("Please enter a numeric value!")
            else:
                print("Please enter a valid option from the menu!")
        except ValueError:
            print("Error, please enter a numeric input!")
        
        print("-" * LINE_WIDTH)
    
    # Assign the correct tax
    while wants_to_order and status not in (0, 1):
        try:
            status = int(input("Are you a staff or a student? (enter 1 for staff, 0 for student): "))
            if status not in (0, 1):
                print("Please enter a valid option for your status!")
        except ValueError:
            print("Error, please enter a numeric input!")

    return order, status

# ------------------------------------------------------
def compute_bill(order, status):
    """
    Computes the total bill amount before and after tax based on order and status.
    
    Args:
        order (dict): Dictionary containing item numbers as keys and quantities as values
        status (int): User's status (0 for student, 1 for staff)
        
    Returns:
        tuple: Contains two elements:
            - bill_before_tax (float): Total amount before tax
            - bill_after_tax (float): Total amount after applying tax (if staff)
    """

    bill_before_tax = sum(MENU[item_num]["price"] * qty for item_num, qty in order.items())
    bill_after_tax = bill_before_tax * (1 + status * TAX)
    return bill_before_tax, bill_after_tax

# ------------------------------------------------------
def print_bill(order, bill_before_tax, bill_after_tax):
    """
    Prints a formatted receipt showing the order details and total amounts.
    
    Args:
        order (dict): Dictionary containing item numbers as keys and quantities as values
        bill_before_tax (float): Total amount before tax
        bill_after_tax (float): Total amount after tax
        
    Returns:
        None
        
    Output:
        Prints a formatted receipt showing:
            - Items ordered with quantities and prices
            - Subtotal (before tax)
            - Tax amount (if applicable)
            - Total amount
    """

    print("\n" + "*" * LINE_WIDTH)
    print("<<" + "-" * ((LINE_WIDTH - 15) // 2) + " Your Bill " + "-" * ((LINE_WIDTH - 15) // 2) + ">>\n")
    
    print(f"{'Item':<{ITEM_WIDTH}} {'Quantity':<{GAP}} {'Price':<{GAP}} {'Total':<{GAP}}")
    print("-" * LINE_WIDTH)

    for item_num, qty in order.items():
        if qty > 0:
            item = MENU[item_num]
            total = item["price"] * qty
            print(f"{item['name']:<{ITEM_WIDTH}} {qty:<{GAP}} ${item['price']:<{GAP-1}} ${round(total, PRECISION):<{GAP-1}}")
    
    print("-" * LINE_WIDTH)
    print(f"{'Bill before tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_before_tax, PRECISION):<{GAP}}")
    print(f"{'Tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax - bill_before_tax, PRECISION):<{GAP}}")
    print(f"{'Bill after tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax, PRECISION):<{GAP}}")
    print(f"{'Total:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax, PRECISION):<{GAP}}")
    print("*" * LINE_WIDTH)

# ------------------------------------------------------
def main():
    
    display_menu()
    quantities, status = get_inputs()

    # Only proceed if the user placed an order
    if sum(quantities.values()) > 0:
        bill_before_tax, bill_after_tax = compute_bill(quantities, status)
        print_bill(quantities, bill_before_tax, bill_after_tax)
    
# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------    



'''
=============================================================
Output 1:
=============================================================

-------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger .................................... $ 5.25
2. Bacon Cheese ...................................... $ 5.75
3. Mushroom Swiss .................................... $ 5.95
4. Western Burger .................................... $ 5.95
5. Con Cali Burger ................................... $ 5.95
6. Exit
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6

Thank you, hope to see you again!
-------------------------------------------------------------
Done!

=============================================================
Output 2:
=============================================================

-------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger .................................... $ 5.25
2. Bacon Cheese ...................................... $ 5.75
3. Mushroom Swiss .................................... $ 5.95
4. Western Burger .................................... $ 5.95
5. Con Cali Burger ................................... $ 5.95
6. Exit
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):      3
How many of Mushroom Swiss would you like to order? 5
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  1
How many of De Anza Burger would you like to order? 2
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  5
How many of Con Cali Burger would you like to order? 4
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6
-------------------------------------------------------------
Are you a staff or a student? (enter 1 for staff, 0 for student): 1

*************************************************************
<<----------------------- Your Bill ----------------------->>

Item                 Quantity     Price        Total       
-------------------------------------------------------------
De Anza Burger       2            $5.25        $10.5       
Mushroom Swiss       5            $5.95        $29.75      
Con Cali Burger      4            $5.95        $23.8       
-------------------------------------------------------------
              Bill before tax:   $64.05       
                          Tax:   $5.76        
               Bill after tax:   $69.81       
                        Total:   $69.81       
*************************************************************
Done!

=============================================================
Output 3:
=============================================================

-------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger .................................... $ 5.25
2. Bacon Cheese ...................................... $ 5.75
3. Mushroom Swiss .................................... $ 5.95
4. Western Burger .................................... $ 5.95
5. Con Cali Burger ................................... $ 5.95
6. Exit
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  de anza burger
Error, please enter a numeric input!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  -7
Please enter a valid option from the menu!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  0
Please enter a valid option from the menu!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  1
How many of De Anza Burger would you like to order? two
Please enter a numeric value!
How many of De Anza Burger would you like to order? -1
Please enter a positive number!
How many of De Anza Burger would you like to order? 2
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6
-------------------------------------------------------------
Are you a staff or a student? (enter 1 for staff, 0 for student): staff
Error, please enter a numeric input!
Are you a staff or a student? (enter 1 for staff, 0 for student): -3
Please enter a valid option for your status!
Are you a staff or a student? (enter 1 for staff, 0 for student): 7
Please enter a valid option for your status!
Are you a staff or a student? (enter 1 for staff, 0 for student): 0

*************************************************************
<<----------------------- Your Bill ----------------------->>

Item                 Quantity     Price        Total       
-------------------------------------------------------------
De Anza Burger       2            $5.25        $10.5       
-------------------------------------------------------------
              Bill before tax:   $10.5        
                          Tax:   $0.0         
               Bill after tax:   $10.5        
                        Total:   $10.5        
*************************************************************
Done!

'''
