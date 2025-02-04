# CIS 41A
# Midterm - part 1
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

# Constant for tax (only for staff)
TAX = 0.09
# Constant for the floating point precision
PRECISION = 2

# Define column widths for the tables in the output
ITEM_WIDTH = 20
QTY_WIDTH = 12
PRICE_WIDTH = 12
TOTAL_WIDTH = 12
LINE_WIDTH = ITEM_WIDTH + QTY_WIDTH + PRICE_WIDTH + TOTAL_WIDTH + 5

# --------------------------------------------------------------------------
def show_menu():
    """
    Displays the menu to the user.
    Args: -
    Returns: -
    """
    print("-" * LINE_WIDTH)
    print("<<" + "-" * ((LINE_WIDTH - 29) // 2) + " De Anza Food Court Menu " + "-" * ((LINE_WIDTH - 29) // 2)+ ">>\n")
    
    for item_num, details in MENU.items():
        dots = "." * (LINE_WIDTH - len(details["name"]) - len(str(details["price"])) - 7)
        print(f"{item_num}. {details['name']} {dots} $ {details['price']}")
    print("6. Exit")
    print("-" * LINE_WIDTH)

# --------------------------------------------------------------------------
def get_inputs():
    
    """
    Gets the user's order and status.
    Args: -
    Returns: -
    """

    # Use dictionary for order quantities
    order = {item_num: 0 for item_num in MENU.keys()}
    status = -1
    wants_to_order = False

    while True:
        try:
            user_choice = int(input("What would you like to order?\n(Enter a number between 1 to 5 to select your order or enter 6 to exit):  "))
            if user_choice == 6:
                break
            
            elif user_choice in MENU:
                wants_to_order = True
                while True:
                    try:
                        item_quantity = int(input(f"How many of {MENU[user_choice]['name']} would you like to order? "))
                        if item_quantity <= 0:
                            print("Please enter a positive number!")
                        else:
                            order[user_choice] += item_quantity
                            break
                    except ValueError:
                        print("Please enter a numeric value!")
            else:
                print("Please enter a valid option from the menu!")
        except ValueError:
            print("Error, please enter a numeric input!")
        
        print("-" * LINE_WIDTH)

    print("-" * LINE_WIDTH)
    
    while wants_to_order and status not in (0, 1):
        try:
            status = int(input("Are you a staff or a student? (enter 1 for staff, 0 for student): "))
            if status not in (0, 1):
                print("Please enter a valid option for your status!")
        except ValueError:
            print("Error, please enter a numeric input!")

    return order, status

# --------------------------------------------------------------------------

def compute_bill(order, status):
    """
    Computes the total amount the user has to pay.
    Args:
        
    Returns: -
    """

    bill_before_tax = sum(MENU[item_num]["price"] * qty for item_num, qty in order.items())
    bill_after_tax = bill_before_tax * (1 + status * TAX)
    return bill_before_tax, bill_after_tax

# --------------------------------------------------------------------------

def print_bill(order, status, bill_before_tax, bill_after_tax):
    """
    Prints the total amount the reciept of the user's order.
    """

    print("\n" + "*" * LINE_WIDTH)
    print("<<" + "-" * ((LINE_WIDTH - 15) // 2) + " Your Bill " + "-" * ((LINE_WIDTH - 15) // 2) + ">>\n")
    
    print(f"{'Item':<{ITEM_WIDTH}} {'Quantity':<{QTY_WIDTH}} {'Price':<{PRICE_WIDTH}} {'Total':<{TOTAL_WIDTH}}")
    print("-" * LINE_WIDTH)

    for item_num, qty in order.items():
        if qty > 0:
            item = MENU[item_num]
            total = item["price"] * qty
            print(f"{item['name']:<{ITEM_WIDTH}} {qty:<{QTY_WIDTH}} ${item['price']:<{PRICE_WIDTH-1}} ${round(total, PRECISION):<{TOTAL_WIDTH-1}}")
    
    print("-" * LINE_WIDTH)
    print(f"{'Bill before tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_before_tax, PRECISION):<{PRICE_WIDTH}}")
    print(f"{'Tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax - bill_before_tax, PRECISION):<{PRICE_WIDTH}}")
    print(f"{'Bill after tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax, PRECISION):<{PRICE_WIDTH}}")
    print(f"{'Total:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax, PRECISION):<{PRICE_WIDTH}}")
    print("*" * LINE_WIDTH)

# --------------------------------------------------------------------------

def main():
    
    show_menu()

    quantities, status = get_inputs()

    bill_before_tax, bill_after_tax = compute_bill(quantities, status)

    # Don't show the bill if they didn't order anything
    if sum(quantities) != 0:
        print_bill(quantities, status, bill_before_tax, bill_after_tax)
    
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
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  3
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
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  de anza
Error, please enter a numeric input!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  -9
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
