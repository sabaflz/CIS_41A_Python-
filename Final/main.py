# CIS 41A
# Final - part 1
# Saba Feilizadeh
# A Menu-Driven Program for De Anza College Food Court
# Using superclasses and subclasses

from person import Student, Staff
from order import Order
from constants import (
    MENU, LINE_WIDTH, MENU_HEADER_PADDING, EXIT_CHOICE,
    STUDENT, STAFF
)
from input_validator import get_menu_choice, get_customer_type, get_quantity
# ------------------------------------------------------ 
def display_menu():
    """
    Display the food court menu with formatting.
    Shows all available items with their prices and the exit option.
    """
    print("-" * LINE_WIDTH)
    print("<<" + "-" * MENU_HEADER_PADDING + " De Anza Food Court Menu " + "-" * MENU_HEADER_PADDING + ">>\n")
    
    for item_num, burger in MENU.items():
        dots = "." * (LINE_WIDTH - len(burger.name) - len(str(burger.price)) - 7)
        print(f"{item_num}. {burger.name} {dots} $ {burger.price}")
    print(f"{EXIT_CHOICE}. Exit")
    print("-" * LINE_WIDTH)
# ------------------------------------------------------ 
def get_order():
    """
    Handle the order process including customer type selection and item ordering.
    
    Returns:
        Order: Complete order object if items were ordered, None if no order was made
    """
    # Dictionary to temporarily store orders before customer type is known
    temp_order = {}  
    wants_to_order = False
    ordering = True

    # Main ordering loop
    while ordering:
        choice = get_menu_choice()
        
        # Handle exit condition
        if choice == EXIT_CHOICE:
            if not wants_to_order:
                print("\nThank you, hope to see you again!")
                return None
            ordering = False
        
        # Process valid menu selections
        if choice in MENU:
            wants_to_order = True
            burger = MENU[choice]
            quantity = get_quantity(burger.name)
            
            # Update quantity if item already exists, otherwise add new item
            if burger in temp_order:
                temp_order[burger] += quantity
            else:
                temp_order[burger] = quantity
                
        print("-" * LINE_WIDTH)

    # Create final order after customer type is determined
    if wants_to_order:
        status = get_customer_type()
        customer = Staff() if status == STAFF else Student()
        order = Order(customer)
        
        # Transfer items from temporary storage to final order
        for burger, quantity in temp_order.items():
            order.add_item(burger, quantity)
        
        return order
    
    return None
# ------------------------------------------------------ 
def main():
    
    display_menu()
    order = get_order()
    
    if order and order.items:
        # Print bill to screen
        print(order.generate_bill())
        
        # Save bill to file
        filename = order.save_bill()
        print(f"\nBill saved to {filename}")
# ------------------------------------------------------ 
if __name__ == "__main__":
    main()
# ------------------------------------------------------ 

'''
========================================================
Output 1:
========================================================
------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger ................................... $ 5.25
2. Bacon Cheese ..................................... $ 5.75
3. Mushroom Swiss ................................... $ 5.95
4. Western Burger ................................... $ 5.95
5. Con Cali Burger .................................. $ 5.95
6. Exit
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): 6

Thank you, hope to see you again!

========================================================
Output 2:
========================================================
------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger ................................... $ 5.25
2. Bacon Cheese ..................................... $ 5.75
3. Mushroom Swiss ................................... $ 5.95
4. Western Burger ................................... $ 5.95
5. Con Cali Burger .................................. $ 5.95
6. Exit
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): 3
How many Mushroom Swisss would you like? 5
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): 1
How many De Anza Burgers would you like? 2
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): 5
How many Con Cali Burgers would you like? 4
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): 6
Are you a staff or student? (1 for staff, 0 for student): 1
************************************************************
<<------------------- Your Bill ------------------->>

Item                 Quantity     Price        Total       
------------------------------------------------------------
Mushroom Swiss       5            $5.95        $29.75      
De Anza Burger       2            $5.25        $10.50      
Con Cali Burger      4            $5.95        $23.80      
------------------------------------------------------------
Bill before tax:                 $      64.05
Tax:                             $       5.76
Total:                           $      69.81
************************************************************

Bill saved to 2025-03-24 13-29-48.txt

========================================================
Output 3:
========================================================
------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger ................................... $ 5.25
2. Bacon Cheese ..................................... $ 5.75
3. Mushroom Swiss ................................... $ 5.95
4. Western Burger ................................... $ 5.95
5. Con Cali Burger .................................. $ 5.95
6. Exit
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): de anza burger
Please enter a valid number!
What would you like to order?
(Enter 1-5 to select, 6 to exit): -7
Please enter a number between 1 and 6!
What would you like to order?
(Enter 1-5 to select, 6 to exit): 0
Please enter a number between 1 and 6!
What would you like to order?
(Enter 1-5 to select, 6 to exit): 1
How many De Anza Burgers would you like? two
Please enter a valid number!
How many De Anza Burgers would you like? -1
Please enter a positive number!
How many De Anza Burgers would you like? 2
------------------------------------------------------------
What would you like to order?
(Enter 1-5 to select, 6 to exit): 6
Are you a staff or student? (1 for staff, 0 for student): staff
Please enter a valid number!
Are you a staff or student? (1 for staff, 0 for student): -3
Please enter 0 or 1!
Are you a staff or student? (1 for staff, 0 for student): 7
Please enter 0 or 1!
Are you a staff or student? (1 for staff, 0 for student): 0
************************************************************
<<------------------- Your Bill ------------------->>

Item                 Quantity     Price        Total       
------------------------------------------------------------
De Anza Burger       2            $5.25        $10.50      
------------------------------------------------------------
Bill before tax:                 $      10.50
Tax:                             $       0.00
Total:                           $      10.50
************************************************************

Bill saved to 2025-03-24 13-30-46.txt

'''