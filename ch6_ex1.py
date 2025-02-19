# CIS 41A
# Ch.6, Ex.1
# Saba Feilizadeh
# Manage two lists of friends that I've encountered in 2017 and 2018. 
# Option to search for a friend, add a friend, and display the lists of friends.

# Constant for the width of the lines in the output
LINE_WIDTH = 50

# Lists of friends I met in 2017 and 2018
friends_2017 = ["Sarah", "Ashkan", "Mina"]
friends_2018 = [ "Nyi", "Carissa", "Josh", "Myra"]

# ------------------------------------------------------
def concatenate_lists():
    """
    Concatenate and display lists of friends from 2017 and 2018.

    Args:
        None
    Returns:
        None
    Output:
        Combines the friends_2017 and friends_2018 lists and prints the result.
    """
    all_my_friends = friends_2017 + friends_2018

    print("-" * LINE_WIDTH)
    print(f"Here is the list of all my friends from 2017 to 2018:\n{all_my_friends}")
    print("-" * LINE_WIDTH)

# ------------------------------------------------------
def find_friend():
    """
    Search for a friend's name in the 2017 and 2018 friend lists.

    Args:
        None
    Returns:
        None
    Output:
        Prompts user for a name and prints which year the friend was met,
        or indicates if the friend was NOT found.
    """
    friend_name = input("Enter a friend's name to search for: ")

    if friend_name in friends_2017:
        print(f"I met {friend_name} in 2017!")

    elif friend_name in friends_2018:
        print(f"I met {friend_name} in 2018!")

    else:
        print(f"{friend_name} is NOT in my list of friends!")

    print("-" * LINE_WIDTH)
# ------------------------------------------------------
def add_friend():
    """
    Add a new friend to either the 2017 or 2018 friend list.

    Args:
        None
    Returns:
        None
    Output:
        Prompts user for friend's name and year met (2017 or 2018),
        then adds the friend to the appropriate list.
    """
    friend_name = input("Enter a friend's name to add to the list: ")

    year_met = input("What year did you meet this friend (Enter 1 for 2017 or 2 for 2018): ")

    if year_met == "1":
        friends_2017.append(friend_name)

    elif year_met == "2":
        friends_2018.append(friend_name)

    else:
        print("Invalid input!")

# ------------------------------------------------------
def display_friends():
    """
    Display the separate lists of friends from 2017 and 2018.

    Args:
        None
    Returns:
        None
    Output:
        Prints both friends_2017 and friends_2018 lists with formatting.
    """
    print("*" * LINE_WIDTH)

    print(f"The list of my friends from 2017:\n{friends_2017}")

    print("-" * LINE_WIDTH)

    print(f"The list of my friends from 2018:\n{friends_2018}")

    print("*" * LINE_WIDTH)

# ------------------------------------------------------
def main():
    # Concatenate and Display the lists
    concatenate_lists()

    # Search for a friend in the list (Ask user for a name)
    find_friend()

    # Add a friend to the friends list (Ask user for a name)
    add_friend()

    # Display the lists of friends (Updated lists)
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
--------------------------------------------------
Here is the list of all my friends from 2017 to 2018:
['Sarah', 'Ashkan', 'Mina', 'Nyi', 'Carissa', 'Josh', 'Myra']
--------------------------------------------------
Enter a friend's name to search for: Nyi
I met Nyi in 2018!
--------------------------------------------------
Enter a friend's name to add to the list: Niloufar
What year did you meet this friend (Enter 1 for 2017 or 2 for 2018): 1
**************************************************
The list of my friends from 2017:
['Sarah', 'Ashkan', 'Mina', 'Niloufar']
--------------------------------------------------
The list of my friends from 2018:
['Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Done!

==========================================================
Output 2:
==========================================================
--------------------------------------------------
Here is the list of all my friends from 2017 to 2018:
['Sarah', 'Ashkan', 'Mina', 'Nyi', 'Carissa', 'Josh', 'Myra']
--------------------------------------------------
Enter a friend's name to search for: George
George is NOT in my list of friends!
--------------------------------------------------
Enter a friend's name to add to the list: Sam
What year did you meet this friend (Enter 1 for 2017 or 2 for 2018): 2
**************************************************
The list of my friends from 2017:
['Sarah', 'Ashkan', 'Mina']
--------------------------------------------------
The list of my friends from 2018:
['Nyi', 'Carissa', 'Josh', 'Myra', 'Sam']
**************************************************
Done!

'''