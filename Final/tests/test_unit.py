# CIS 41A
# Final - part 1
# Saba Feilizadeh

import unittest
from burger import DeAnzaBurger, BaconCheese
from person import Student, Staff
from order import Order
from constants import STUDENT_TAX_RATE, STAFF_TAX_RATE

"""
Unit tests for the De Anza Burger ordering system.

This module contains unit tests that verify the individual components
of the system work correctly in isolation. It tests the basic functionality
of the Burger, Person, and Order classes.

Classes:
    TestBurger: Tests burger properties and initialization
    TestPerson: Tests customer type properties and tax rates
    TestOrder: Tests order management operations
"""

class TestBurger(unittest.TestCase):
    def test_burger_properties(self):
        """Test burger name and price are set correctly"""
        burger = DeAnzaBurger()
        self.assertEqual(burger.name, "De Anza Burger")
        self.assertEqual(burger.price, 5.25)

class TestPerson(unittest.TestCase):
    def test_student_tax_rate(self):
        """Test student tax rate is set correctly"""
        student = Student()
        self.assertEqual(student.tax_rate, STUDENT_TAX_RATE)

    def test_staff_tax_rate(self):
        """Test staff tax rate is set correctly"""
        staff = Staff()
        self.assertEqual(staff.tax_rate, STAFF_TAX_RATE)

class TestOrder(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.student = Student()
        self.staff = Staff()
        self.burger1 = DeAnzaBurger()
        self.burger2 = BaconCheese()

    def test_add_item(self):
        """Test adding items to order"""
        order = Order(self.student)
        order.add_item(self.burger1, 2)
        self.assertEqual(order.get_item_quantity(self.burger1), 2)

    def test_update_item_quantity(self):
        """Test updating item quantity"""
        order = Order(self.student)
        order.add_item(self.burger1, 2)
        order.update_item_quantity(self.burger1, 3)
        self.assertEqual(order.get_item_quantity(self.burger1), 3)

    def test_remove_item(self):
        """Test removing item from order"""
        order = Order(self.student)
        order.add_item(self.burger1, 2)
        order.remove_item(self.burger1)
        self.assertEqual(order.get_item_quantity(self.burger1), 0)

    def test_calculate_student_total(self):
        """Test order total calculation for student (no tax)"""
        order = Order(self.student)
        order.add_item(self.burger1, 2)  # 2 * $5.25 = $10.50
        self.assertEqual(order.calculate_total(), 10.50)

    def test_calculate_staff_total(self):
        """Test order total calculation for staff (with tax)"""
        order = Order(self.staff)
        order.add_item(self.burger1, 2)  # 2 * $5.25 = $10.50 + 9% tax
        self.assertAlmostEqual(order.calculate_total(), 11.445)

if __name__ == '__main__':
    unittest.main() 