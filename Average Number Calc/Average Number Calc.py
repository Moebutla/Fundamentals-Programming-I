#####
#
#   Average Number Calculator
#   Author: Mose Butler
#   Date: November 10, 2018
#   Version: 1.0.0
#
#####

# This program takes in a .txt file with numbers and finds the average of the numbers.

# Calculates an average of the values in a list
def averageCalc (list):
    return sum(list) / len(list)

# Global test variables
isFile = False
isReading = True
hasLetter = False
numbersFromFile = []  # Empty list to be used for file values

# Gathers names of file and checks that file exists.
while not isFile:
    try:
        userFileName = input("Enter file name (do not include .txt): ") + ".txt"
        userFile = open(userFileName)  # opens file
        isFile = True
    except FileNotFoundError:  # If file does not exist, asks again.
        print("File does not exist, please try again.\n")
        isFile = False

# Pulls data from file until there are no more values to pull
while isReading:
    rawData = userFile.readline()
    rawData = rawData.rstrip().split(" ")
    if rawData[0] != "":  # Checks to see if line was blank
        try:
            numbersFromFile.append(int(rawData[0]))  # Converts value to int and adds to list
        except ValueError:  # If value is not a number, stops loop
            print("File contains non-numerical values. Please use a different file.")
            hasLetter = True
            isReading = False
    else:  # If row is empty, ends loop
        isReading = False

userFile.close()  # Closes file

# checks that file had at least one value and if there was a non-numerical value
if (len(numbersFromFile) > 0) and (hasLetter is False):
    print("The average number is: %d" % averageCalc(numbersFromFile))
else:
    print("Program terminated.")

