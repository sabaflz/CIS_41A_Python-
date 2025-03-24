# CIS 41A
# Final - part 1
# Saba Feilizadeh

from datetime import datetime
from constants import (
    LINE_WIDTH, BILL_HEADER_PADDING, ITEM_NAME_WIDTH,
    QUANTITY_WIDTH, PRICE_WIDTH, TOTAL_WIDTH,
    PRICE_LABEL_WIDTH, BILLS_DIRECTORY
)

class Order:
    def __init__(self, customer):
        self._customer = customer
        self._items = {}
        self._order_time = datetime.now()

    @property
    def customer(self):
        return self._customer

    @property
    def items(self):
        return self._items

    @property
    def order_time(self):
        return self._order_time
# ------------------------------------------------------ 
    def add_item(self, burger, quantity):
        """
        Add a new item to the order or update quantity if it already exists.

        Args:
            burger (Burger): The burger object to add to the order
            quantity (int): The quantity of burgers to add

        Example:
            >>> order.add_item(DeAnzaBurger(), 2)
        """
        if burger in self._items:
            self._items[burger] += quantity
        else:
            self._items[burger] = quantity
# ------------------------------------------------------ 
    def calculate_subtotal(self):
        """
        Calculate the subtotal of all items before tax.
        
        Returns:
            float: The subtotal amount
        """
        return sum(burger.price * quantity for burger, quantity in self._items.items())
# ------------------------------------------------------ 
    def calculate_tax(self):
        """
        Calculate the tax amount based on the subtotal and customer type.
        
        Returns:
            float: The tax amount
        """
        return self.calculate_subtotal() * self._customer.tax_rate
# ------------------------------------------------------ 
    def calculate_total(self):
        """
        Calculate the total amount including tax.
        
        Returns:
            float: The total amount
        """
        return self.calculate_subtotal() + self.calculate_tax()
# ------------------------------------------------------ 
    def generate_bill(self):
        """
        Generate a formatted bill string showing all items, quantities, prices,
        subtotal, tax, and total.
        
        Returns:
            str: The formatted bill as a string
        """
        bill = []
        # Add header decorations
        bill.append("*" * LINE_WIDTH)
        bill.append("<<" + "-" * BILL_HEADER_PADDING + " Your Bill " + "-" * BILL_HEADER_PADDING + ">>\n")
        
        # Add column headers
        bill.append(f"{'Item':<{ITEM_NAME_WIDTH}} {'Quantity':<{QUANTITY_WIDTH}} {'Price':<{PRICE_WIDTH}} {'Total':<{TOTAL_WIDTH}}")
        bill.append("-" * LINE_WIDTH)

        # Add individual items
        for burger, quantity in self._items.items():
            total = burger.price * quantity
            bill.append(f"{burger.name:<{ITEM_NAME_WIDTH}} {quantity:<{QUANTITY_WIDTH}} ${burger.price:<{PRICE_WIDTH-1}} ${total:<{TOTAL_WIDTH-1}.2f}")

        # Add totals section
        bill.append("-" * LINE_WIDTH)
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        bill.append(f"{'Bill before tax:':<{PRICE_LABEL_WIDTH}} ${subtotal:>11.2f}")
        bill.append(f"{'Tax:':<{PRICE_LABEL_WIDTH}} ${tax:>11.2f}")
        bill.append(f"{'Total:':<{PRICE_LABEL_WIDTH}} ${total:>11.2f}")
        bill.append("*" * LINE_WIDTH)
        
        return "\n".join(bill)
# ------------------------------------------------------ 
    def save_bill(self, filename=None):
        """
        Save the generated bill to a file.
        
        Args:
            filename (str, optional): Custom filename for the bill.
                If None, generates a filename using the current timestamp.
                
        Returns:
            str: The filename where the bill was saved
        """
        if filename is None:
            filename = f"{self._order_time.strftime('%Y-%m-%d %H-%M-%S')}.txt"
        
        with open(BILLS_DIRECTORY + filename, 'w') as f:
            f.write(self.generate_bill())
        return filename
# ------------------------------------------------------ 
    def get_item_quantity(self, burger):
        """
        Get the quantity of a specific burger in the order.

        Args:
            burger (Burger): The burger object to look up

        Returns:
            int: The quantity of the specified burger (0 if not in order)

        Example:
            >>> order.get_item_quantity(DeAnzaBurger())
            2
        """
        return self._items.get(burger, 0)
# ------------------------------------------------------ 
    def update_item_quantity(self, burger, new_quantity):
        """
        Update the quantity of an existing item in the order.
        If new quantity is 0 or negative, the item will be removed.

        Args:
            burger (Burger): The burger object to update
            new_quantity (int): The new quantity to set

        Example:
            >>> order.update_item_quantity(DeAnzaBurger(), 3)
        """
        if new_quantity > 0:
            self._items[burger] = new_quantity
        else:
            self.remove_item(burger)
# ------------------------------------------------------ 
    def remove_item(self, burger):
        """
        Remove an item completely from the order.

        Args:
            burger (Burger): The burger object to remove

        Raises:
            KeyError: If the burger is not in the order

        Example:
            >>> order.remove_item(DeAnzaBurger())
        """
        if burger in self._items:
            del self._items[burger]