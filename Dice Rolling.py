#Import 'random' Package
import random
arrCounter = [0, 0, 0, 0, 0, 0, 0]
#Function to check if input string is valid
def check_input(inpString):
    success = False
    if inpString.isdigit():
        success = True
    return success

#Function to randomly roll a dice
def roll_dice():
    #Generates number between 1 (inclusive) and 7 (exclusive)
    result = random.randint(1,6)
    #Returns results of dice roll
    return result

#Function to ask input
def ask_user_input():
    inpUserGuess = input("How many times do you want to roll the die? ")
    checkSuccess = check_input(inpUserGuess)
    #If input is invalid (not int), the while loop will ask for valid input
    while checkSuccess == False:
        print("Invalid input. Please input a valid integer.")
        inpUserGuess = input("How many times do you want to roll the die? ")
        if check_input(inpUserGuess):
            checkSuccess = True      
    return inpUserGuess

#Takes input for amount of times the user wants to roll the dice
inpUser = ask_user_input()
#Performs roll equal to the number from input
for i in range(int(inpUser)):
    strResult = "Dice #{} has rolled a {}"
    print(strResult.format(str(i+1), str(roll_dice())))


