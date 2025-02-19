# CIS 41A
# Ch.6, Ex.2
# Saba Feilizadeh
# Manage a dictionary containing friends that I've encountered in 2017 and 2018. 
# Option to search for a friend, add a friend, and display the lists of friends.

# Constant for the width of the line for the output
LINE_WIDTH = 50

# A dictionary representing friends I met in 2017 and 2018
friends_dict = {
    "2017" : ["Sarah", "Ashkan", "Mina"],
    "2018" : [ "Nyi", "Carissa", "Josh", "Myra"],
}

# ------------------------------------------------------ 
def find_friend():
    """
    Search for a friend's name in the friends dictionary and print which year they were met.

    Args:
        None
    Returns:
        None
    Output:
        Prompt the user to enter a name and print whether the friend was met in 2017,
        2018, or was not found in the dictionary.
    """

    friend_name = input("Enter a friend's name to search for: ")

    if friend_name in friends_dict["2017"]:
        print(f"I met {friend_name} in 2017!")

    elif friend_name in friends_dict["2018"]:
        print(f"I met {friend_name} in 2018!")

    else:
        print(f"{friend_name} is NOT in my list of friends!")

    print("-" * LINE_WIDTH)

# ------------------------------------------------------ 
def add_friend():
    """
    Add a new friend to the friends dictionary.

    Args:
        None
    Returns:
        None
    Output:
        Prompt the user for friend's name and year met (2017 or 2018),
        then add the friend to the appropriate key in the dictionary.
    """
    friend_name = input("Enter a friend's name to add to the dictionary: ")

    year_met = input("What year did you meet this friend (Enter 1 for 2017 or 2 for 2018): ")

    if year_met == "1":
        friends_dict["2017"].append(friend_name)

    elif year_met == "2":
        friends_dict["2018"].append(friend_name)

    else:
        print("Invalid input!")

# ------------------------------------------------------
def display_friends():
    """
    Display the complete list of friends organized by year.

    Args:
        None
    Returns:
        None
    Output:
        Prints a formatted output showing all friends met in 2017 and 2018.
    """
    print("*" * LINE_WIDTH)
    print("-" * (LINE_WIDTH // 2))

    print("The list of friends")

    print("-" * (LINE_WIDTH // 2))

    print(f"From 2017:\n{friends_dict["2017"]}")

    print(f"From 2018:\n{friends_dict["2018"]}")

    print("*" * LINE_WIDTH)

# ------------------------------------------------------
def main():
    # Display the lists of friends from the dictionary (Original)
    display_friends()

    # Search for a friend in the dictionary (Ask user for a name)
    find_friend()

    # Add a friend to the dictionary (Ask user for a name)
    add_friend()

    # Display the lists of friends from the dictionary (Updated)
    display_friends()
    

# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------ 
'''
==========================================================
Output 1:
==========================================================
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Sarah', 'Ashkan', 'Mina']
From 2018:
['Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Enter a friend's name to search for: Nyi
I met Nyi in 2018!
--------------------------------------------------
Enter a friend's name to add to the dictionary: Niloufar
What year did you meet this friend (Enter 1 for 2017 or 2 for 2018): 1
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Sarah', 'Ashkan', 'Mina', 'Niloufar']
From 2018:
['Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Done!

==========================================================
Output 2:
==========================================================
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Sarah', 'Ashkan', 'Mina']
From 2018:
['Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Enter a friend's name to search for: George
George is NOT in my list of friends!
--------------------------------------------------
Enter a friend's name to add to the dictionary: Sam 
What year did you meet this friend (Enter 1 for 2017 or 2 for 2018): 2
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Sarah', 'Ashkan', 'Mina']
From 2018:
['Nyi', 'Carissa', 'Josh', 'Myra', 'Sam']
**************************************************
Done!

'''