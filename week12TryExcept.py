#!/usr/bin/env python

# try...except statement for input of numbers 
try:
    myNumber = input("Enter your number here: ") # user prompted to enter any number
    assert (myNumber >= 50) # Testing that number is greater than/equal to 50
except AssertionError: # If the number is not greater than/equal to 50
    print("This number is too small. Try again. ") # This message is printed