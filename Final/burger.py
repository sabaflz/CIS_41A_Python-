# CIS 41A
# Final - part 1
# Saba Feilizadeh

class Burger:
    """Base class for all burgers"""
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
# ------------------------------------------------------ 
class DeAnzaBurger(Burger):
    def __init__(self):
        super().__init__("De Anza Burger", 5.25)
# ------------------------------------------------------ 
class BaconCheese(Burger):
    def __init__(self):
        super().__init__("Bacon Cheese", 5.75)
# ------------------------------------------------------ 
class MushroomSwiss(Burger):
    def __init__(self):
        super().__init__("Mushroom Swiss", 5.95)
# ------------------------------------------------------ 
class WesternBurger(Burger):
    def __init__(self):
        super().__init__("Western Burger", 5.95)
# ------------------------------------------------------ 
class ConCaliBurger(Burger):
    def __init__(self):
        super().__init__("Con Cali Burger", 5.95)