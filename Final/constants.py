# CIS 41A
# Final - part 1
# Saba Feilizadeh

from burger import DeAnzaBurger, BaconCheese, MushroomSwiss, WesternBurger, ConCaliBurger

MENU = {
    1: DeAnzaBurger(),
    2: BaconCheese(),
    3: MushroomSwiss(),
    4: WesternBurger(),
    5: ConCaliBurger()
}

# Menu-related constants
MENU_MIN_CHOICE = 1
MENU_MAX_CHOICE = 5
EXIT_CHOICE = 6

# Display formatting constants for bill and menu layout
LINE_WIDTH = 60
MENU_HEADER_PADDING = 16
BILL_HEADER_PADDING = 19
ITEM_NAME_WIDTH = 20
QUANTITY_WIDTH = 12
PRICE_WIDTH = 12
TOTAL_WIDTH = 12
PRICE_LABEL_WIDTH = 32

# Customer type identifiers
STUDENT = 0
STAFF = 1

# Customer tax rate
STUDENT_TAX_RATE = 0.00
STAFF_TAX_RATE = 0.09

# File system constants
BILLS_DIRECTORY = 'Final/'