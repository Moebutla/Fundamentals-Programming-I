#####
#
#   Secondary color generator
#   Author: Mose Butler
#   Date: September 22, 2018
#   Version: 1.0
#
#####

# Instructions to user
print("The colors red, blue, and yellow are considered \'primary colors\', because they cannot be created by other "
      "colors.")
print("When you mix primary colors, you get secondary colors.\n")

# Declaring variables based on user input
# Takes input then checks to make sure it matches primary colors of red, blue, yellow. Will continue to ask until
# valid entry. Case sensitive
firstColor = input("Enter your first primary color (red, yellow, blue): ")
while firstColor != "red" and firstColor != "blue" and firstColor != "yellow":
    firstColor = input("Enter your first primary color (red, yellow, blue): ")

# Takes input then checks to make sure it matches primary colors of red, blue, yellow. Then checks to makes sure
# that it does not match firstColor variable. Will continue to ask until valid entry. Case sensitive
secondColor = input("Enter your second primary color (red, yellow, blue): ")
while (secondColor != "red" and secondColor != "blue" and secondColor != "yellow") or secondColor == firstColor:
    secondColor = input("Enter your second primary color (red, yellow, blue): ")

# Processing user input and calculating output. Checks for purple, green, then orange.
if (firstColor == "red" and secondColor == "blue") or (firstColor == "blue" and secondColor == "red"):
    print("If you mix %s and %s, you get purple!" % (firstColor, secondColor))
elif (firstColor == "blue" and secondColor == "yellow") or (firstColor == "yellow" and secondColor == "blue"):
    print("If you mix %s and %s, you get green!" % (firstColor, secondColor))
else:
    print("If you mix %s and %s, you get orange!" % (firstColor, secondColor))


