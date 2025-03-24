# CIS 41A
# Final - part 1
# Saba Feilizadeh

def get_integer_input(prompt, min_value=None, max_value=None, error_message=None):
    """
    Get and validate integer input from the user.
    
    Args:
        prompt (str): The message to display when asking for input
        min_value (int, optional): Minimum acceptable value
        max_value (int, optional): Maximum acceptable value
        error_message (str, optional): Custom error message for invalid range
        
    Returns:
        int: The validated integer input
    """
    valid_input = False
    while not valid_input:
        try:
            # Attempt to convert input to integer
            value = int(input(prompt))
            
            # Check if value is within acceptable range
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(error_message or f"Please enter a number between {min_value} and {max_value}!")
                continue
            valid_input = True
            return value
        except ValueError:
            print("Please enter a valid number!")
# ------------------------------------------------------ 
def get_customer_type():
    """
    Get and validate the customer type (staff or student).
    
    Returns:
        int: 0 for student, 1 for staff
    """
    from constants import STUDENT, STAFF
    prompt = "Are you a staff or student? (1 for staff, 0 for student): "
    error_msg = "Please enter 0 or 1!"
    return get_integer_input(prompt, STUDENT, STAFF, error_msg)
# ------------------------------------------------------ 
def get_menu_choice():
    """
    Get and validate the menu selection from the user.
    
    Returns:
        int: Menu item number (1-5) or exit choice (6)
    """
    from constants import MENU_MIN_CHOICE, MENU_MAX_CHOICE, EXIT_CHOICE
    prompt = "What would you like to order?\n(Enter 1-5 to select, 6 to exit): "
    return get_integer_input(prompt, MENU_MIN_CHOICE, EXIT_CHOICE)
# ------------------------------------------------------ 
def get_quantity(item_name):
    """
    Get and validate the quantity for a menu item.
    
    Args:
        item_name (str): Name of the item being ordered
        
    Returns:
        int: Quantity of items to order (positive integer)
    """
    prompt = f"How many {item_name}s would you like? "
    return get_integer_input(prompt, 1, None, "Please enter a positive number!") 