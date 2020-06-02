# Pickling and Error Handling
*PO'Brien, 6.1.2020*

## Introduction
This document covers my process for approaching module 7 and completing the seventh assignment of IT FDN 100 A.

## Initial Learning
As per usual, I watched the corresponding course video by Randal, read through the textbook chapter 7, and then I found two external sources, datacamp for pickling and w3schools for error handling.

## Creating Pickling Code
I did this assignment in two steps. The first step was creating a simple script that demonstrated how I could take user inputs and pickle them into a binary file, and then un-pickle that binary file to read that data back to the user. I found examples in the course textbook as well as datacamp to be helpful in learning how pickling works. I found that datacamp has excellent step by step examples as well as descriptions of how and when it is useful to use pickling.


```
import pickle

userInput = input("Would you like to store your data in binary format? (y/n): ")

if userInput.lower() == "y":
    userName = input("Enter your name: ")
    userAge = int(input("Enter your age: "))
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
```
## Adding Error Handling
I decided to add a simple error handling feature that flags if the user does not enter an integer for his or her name. To do so, I used the Try, Except, and Else keywords as show in (figure 2) below. I found the demonstrations of this error handling capability on w3schools to be very easy to follow and understand. As shown in (figure 2) I have the try keyword above the userAge input, and if it detects a value error the except function prints the nature of the problem and terminates the program.

```
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
```

## Running Program
![Running in PyCharm](https://github.com/POB768/IntroToProg-Python-Mod07/blob/master/docs/Running%20in%20PyCharm.png "Running in PyCharm")

