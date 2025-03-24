# CIS 41A
# Final - part 1
# Saba Feilizadeh

import unittest
import os
from datetime import datetime
from person import Student, Staff
from burger import DeAnzaBurger, BaconCheese
from order import Order
from constants import BILLS_DIRECTORY

"""
Integration tests for the De Anza Burger ordering system.

This module contains integration tests that verify different components
of the system work together correctly. It tests complete order workflows
from creation to bill generation and saving.

Test Workflows:
    - Complete student order flow (no tax)
    - Complete staff order flow (with tax)
    - Bill generation and file saving
"""

class TestOrderingSystem(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.student = Student()
        self.staff = Staff()
        self.burger1 = DeAnzaBurger()
        self.burger2 = BaconCheese()

    def test_complete_student_order_flow(self):
        """
        Test complete order flow for a student:
        1. Create order
        2. Add multiple items
        3. Update quantities
        4. Generate bill
        5. Save bill to file
        """
        # Create order
        order = Order(self.student)
        
        # Add items
        order.add_item(self.burger1, 2)
        order.add_item(self.burger2, 1)
        
        # Update quantity
        order.update_item_quantity(self.burger1, 3)
        
        # Verify order contents
        self.assertEqual(order.get_item_quantity(self.burger1), 3)
        self.assertEqual(order.get_item_quantity(self.burger2), 1)
        
        # Check bill generation
        bill = order.generate_bill()
        self.assertIn("De Anza Burger", bill)
        self.assertIn("Bacon Cheese", bill)
        
        # Verify calculations
        expected_total = (3 * self.burger1.price + 1 * self.burger2.price)
        self.assertEqual(order.calculate_total(), expected_total)
        
        # Test bill saving
        filename = order.save_bill()
        self.assertTrue(os.path.exists(BILLS_DIRECTORY + filename))
        
        # Clean up test file
        os.remove(BILLS_DIRECTORY + filename)

    def test_complete_staff_order_flow(self):
        """
        Test complete order flow for staff:
        1. Create order
        2. Add items
        3. Remove items
        4. Verify tax calculation
        5. Generate and save bill
        """
        # Create order
        order = Order(self.staff)
        
        # Add and remove items
        order.add_item(self.burger1, 2)
        order.add_item(self.burger2, 2)
        order.remove_item(self.burger2)
        
        # Verify order contents
        self.assertEqual(order.get_item_quantity(self.burger1), 2)
        self.assertEqual(order.get_item_quantity(self.burger2), 0)
        
        # Check tax calculations
        subtotal = 2 * self.burger1.price
        expected_total = subtotal * (1 + self.staff.tax_rate)
        self.assertAlmostEqual(order.calculate_total(), expected_total)
        
        # Test bill generation and saving
        bill = order.generate_bill()
        self.assertIn("Tax:", bill)
        
        filename = order.save_bill()
        self.assertTrue(os.path.exists(BILLS_DIRECTORY + filename))
        
        # Clean up test file
        os.remove(BILLS_DIRECTORY + filename)

if __name__ == '__main__':
    unittest.main() 