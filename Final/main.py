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
from input_validator import get_menu_choice, get_customer_type, get_quantity, get_integer_input
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
    Handle the order process with full CRUD (Create, Read, Update, Delete) operations.
    
    Provides an interactive menu that allows users to:
    1. Add new items (Create)
    2. View current order (Read)
    3. Update item quantities (Update)
    4. Remove items (Delete)
    5. Finish the order
    6. Cancel the order
    
    Returns:
        Order: Complete order object if items were ordered and confirmed
        None: If the order was cancelled or no items were ordered
        
    Example:
        >>> order = get_order()
        >>> if order:
        >>>     print(order.generate_bill())
    """
    temp_order = {}  # Dictionary to temporarily store orders before customer type is known
    wants_to_order = False
    ordering = True

    while ordering:
        print("\n1. Add item")
        print("2. Update item quantity")
        print("3. Remove item")
        print("4. View current order")
        print("5. Finish order")
        print("6. Cancel order")
        
        choice = get_integer_input("Enter your choice (1-6): ", 1, 6)
        
        if choice == 1:  # CREATE
            display_menu()
            item_choice = get_menu_choice()
            if item_choice in MENU:
                burger = MENU[item_choice]
                quantity = get_quantity(burger.name)
                if burger in temp_order:
                    temp_order[burger] += quantity
                else:
                    temp_order[burger] = quantity
                wants_to_order = True
                
        elif choice == 2:  # UPDATE
            if temp_order:
                print("\nCurrent items:")
                # Create a numbered list of items
                items = list(temp_order.items())
                for idx, (burger, qty) in enumerate(items, 1):
                    print(f"{idx}. {burger.name}: {qty}")
                
                # Get item selection
                item_idx = get_integer_input("Select item number to update (or 0 to cancel): ", 0, len(items))
                if item_idx > 0:
                    burger, current_qty = items[item_idx - 1]
                    print(f"Current quantity for {burger.name}: {current_qty}")
                    new_qty = get_integer_input("Enter new quantity (0 to remove): ", 0, None)
                    
                    if new_qty == 0:
                        del temp_order[burger]
                        print(f"\n{burger.name} removed from order")
                    else:
                        temp_order[burger] = new_qty
                        print(f"\n{burger.name} quantity updated to {new_qty}")
            else:
                print("\nOrder is empty! Nothing to update.")
                
        elif choice == 3:  # DELETE
            if temp_order:
                print("\nSelect item to remove:")
                items = list(temp_order.items())
                for idx, (burger, qty) in enumerate(items, 1):
                    print(f"{idx}. {burger.name}: {qty}")
                
                item_idx = get_integer_input("Select item number to remove (or 0 to cancel): ", 0, len(items))
                if item_idx > 0:
                    burger, _ = items[item_idx - 1]
                    del temp_order[burger]
                    print(f"\n{burger.name} removed from order")
            else:
                print("\nOrder is empty! Nothing to remove.")
                
        elif choice == 4:  # READ
            if temp_order:
                print("\nCurrent order:")
                for burger, qty in temp_order.items():
                    print(f"{burger.name}: {qty} - ${burger.price * qty:.2f}")
            else:
                print("\nOrder is empty")
                
        elif choice == 5:  # Finish order
            if wants_to_order:
                ordering = False
            else:
                print("\nOrder is empty!")
                
        elif choice == 6:  # Cancel order
            print("\nOrder cancelled")
            return None
            
        print("-" * LINE_WIDTH)

    # Create final order after customer type is determined
    if wants_to_order:
        status = get_customer_type()
        customer = Staff() if status == STAFF else Student()
        order = Order(customer)
        
        for burger, quantity in temp_order.items():
            order.add_item(burger, quantity)
        
        return order
    
    return None
# ------------------------------------------------------ 
def main():
    """
    Main program entry point that handles the complete ordering process.
    
    Flow:
    1. Displays the menu
    2. Gets the order with CRUD operations
    3. If order exists:
        - Generates and displays the bill
        - Saves the bill to a file
    
    Example:
        >>> if __name__ == "__main__":
        >>>     main()
    """
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

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 6

Order cancelled

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

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 1
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

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 1
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
(Enter 1-5 to select, 6 to exit): 1
How many De Anza Burgers would you like? 2
------------------------------------------------------------

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 1
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
(Enter 1-5 to select, 6 to exit): 5
How many Con Cali Burgers would you like? 4
------------------------------------------------------------

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 4

Current order:
Mushroom Swiss: 5 - $29.75
De Anza Burger: 2 - $10.50
Con Cali Burger: 4 - $23.80
------------------------------------------------------------

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 5
------------------------------------------------------------
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

Bill saved to 2025-03-24 13-46-41.txt

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

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 1
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

1. Add item
2. Update item quantity
3. Remove item
4. View current order
5. Finish order
6. Cancel order
Enter your choice (1-6): 5
------------------------------------------------------------
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

Bill saved to 2025-03-24 13-49-41.txt

'''