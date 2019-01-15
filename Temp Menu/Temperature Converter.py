1#######
#
# Temperature Converter
# Author: Mose Butler
# Date: 10-26-18
# Version: 1.0.0
#
#######

# Setting Global Variables
CONVERSION_CONSTANT = 32
CELSIUS_CONVERSION = 5/9
FAHRENHEIT_CONVERSION = 1.8
done = False


# Function converts fahrenheit to celsius
def fahrenheit_to_celsius(temperature):
    return (temperature - CONVERSION_CONSTANT) * CELSIUS_CONVERSION


# Function converts celsius to fahrenheit
def celsius_to_fahrenheit(temperature):
    return temperature * FAHRENHEIT_CONVERSION + CONVERSION_CONSTANT


# Quick explanation of program
print("This program converts temperature from fahrenheit to celsius or celsius to fahrenheit."
      "\nEnter a value from a menu to start the program.")

# Asks user for command based on menu options. Runs until user is finished with program.
while not done:
    menuCheck = input("\n[1] Convert celsius to fahrenheit."
                      "\n[2] Convert fahrenheit to celsius."
                      "\n[3] Exit program."
                      "\n\nEnter Command: ")

    # Compares user input to expected inputs
    if menuCheck == '1':  # if user input matches will run celsius to fahrenheit function and continue loop
        temperatureCelsius = float(input("Enter temperature in celsius: "))
        convertedTemp = celsius_to_fahrenheit(temperatureCelsius)
        print("%0.2fC converts to %0.2fF." % (temperatureCelsius, convertedTemp))

    elif menuCheck == '2':  # if user input matches will run fahrenheit to celsius function and continue loop
        temperatureFahrenheit = float(input("Enter temperature in fahrenheit: "))
        convertedTemp = fahrenheit_to_celsius(temperatureFahrenheit)
        print("%0.2fF converts to %0.2fC." % (temperatureFahrenheit, convertedTemp))

    elif menuCheck == '3':  # if user input matches will terminate program
        done = True

    else:  # if user input is not recognized, will print statement and ask again
        print("Entry not valid.")

print("Program Terminated.")
