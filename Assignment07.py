# ------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Error Handling Demo Script
# ChangeLog: (Who, When, What)
# PO'Brien,6.1.2020,Created Script
# PO'Brien,6.1.2020,Added Pickling Code
# PO'Brien,6.1.2020,Added Exception Handling Code
# ------------------------------------------------- #

import pickle
import sys  # imported so program can cancel when error occurs


userInput = input("Would you like to store your data in binary format? (y/n): ")

if userInput.lower() == "y":
    userName = input("Enter your name: ")
    try:
        userAge = int(input("Enter your age: "))
    except ValueError:      # produces error message if user does not enter an int for age
        print('Error: age must be an integer')
        sys.exit()  # stops program if error occurs
    else:
        userJob = input("Enter your occupation: ")
        userHobby = input("Enter your favorite hobby: ")
        userList = [userName, userAge, userJob, userHobby]      # aggregates user inputs into list

        print()  # extra line for looks
        print(userList)
        userInput2 = input("This is your data, would you now like to store it in binary via Pickling? (y/n): ")

        if userInput2.lower() == "y":
            pickleFile = open("pickles.dat", "wb")  # opening new pickleFile in write mode
            pickle.dump(userList, pickleFile)       # dumping user list into pickleFile
            pickleFile.close()
            print()     # extra line for looks
            print("Your data has been Pickled!")
            userInput3 = input("Would you like to un-pickle your file and read it? (y/n): ")
            if userInput3.lower() == "y":
                pickleFile = open("pickles.dat", "rb")      # opening the binary file to read
                userList = pickle.load(pickleFile)          # loading file contents into list
                print()     # space for aesthetic
                print("Here is your un-pickled list!")  # output for the user to view
                print(userList)  # output for the user to view
                print("Goodbye!")
                pickleFile.close()
            elif userInput3.lower() == "n":
                print("Your data remains pickled, goodbye!")

        elif userInput2.lower() == "n":
            print("Goodbye!")

elif userInput.lower() == "n":
    print("Goodbye!")

