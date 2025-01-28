# CIS 41A
# Ch.4, Ex.1
# Saba Feilizadeh
# Get the user's email address and validate it
# Print the domain of the email address

# ------------------------------------------------------
def main():

    valid = False
    while not valid:
        # Get input values
        email = input("Enter your email: ")

        # valid email address
        if '@' in email and '.' in email:
            at_position = email.find('@')
            dot_position = email.find('.')

            # correct order for '@' and '.'
            if at_position < dot_position:
                valid = True
                domain = email[at_position + 1 : dot_position]
                print(domain)

        # invalid email address
        else:
            print('Error! Please enter a valid email address!')
   


# ------------------------------------------------------
if __name__ == "__main__":
    main()
    print("Done!")
# ------------------------------------------------------

'''
Outputs:

Enter your email: joe@yahoo.com
yahoo
Done!

------------------

Enter your email: stevejob
Error! Please enter a valid email address!
Enter your email: steve.jobs
Error! Please enter a valid email address!
Enter your email: steve@apple     
Error! Please enter a valid email address!
Enter your email: steve.jobs@apple
Enter your email: steve@apple.jobs
apple
Done!

'''