# CIS 41A
# Final - part 1
# Saba Feilizadeh

from constants import STUDENT_TAX_RATE, STAFF_TAX_RATE

class Person:
    """Base class for all customers"""
    def __init__(self):
        self._tax_rate = 0.0

    @property
    def tax_rate(self):
        return self._tax_rate
# ------------------------------------------------------ 
class Student(Person):
    def __init__(self):
        super().__init__()
        self._tax_rate = STUDENT_TAX_RATE
# ------------------------------------------------------ 
class Staff(Person):
    def __init__(self):
        super().__init__()
        self._tax_rate = STAFF_TAX_RATE