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
        Add or update an item in the order.
        
        Args:
            burger (Burger): The burger to add to the order
            quantity (int): The quantity to add
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
            filename = f"bill_{self._order_time.strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(BILLS_DIRECTORY + filename, 'w') as f:
            f.write(self.generate_bill())
        return filename