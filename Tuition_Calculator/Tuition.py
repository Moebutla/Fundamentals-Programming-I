####
#   Tuition Increase Calculator
#   Author: Mose Butler
#   Date: 10/13/18
#   Version: 1.0.0
####

# Declaring Variables
tuitionRate = 8000
i = 0
yearsTesting = 5
percentIncrease = 0.03

# print starting tuition rate
print("Tuition for school this year is $%d." % tuitionRate)

# Loop runs 5 times, increasing tuition by 3% each year.
while i < yearsTesting:
    tuitionRate += tuitionRate * percentIncrease
    print("In %d year(s), your tuition will be $%d." % (i + 1, tuitionRate))

    i += 1


