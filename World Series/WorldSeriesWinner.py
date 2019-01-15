#######
##
#   World Series Winners
#   Author: Mose Butler
#   Date: 11/18/18
#   Version: 1.0.0
##
#######

# import numpy library for easy reading from .txt file
import numpy as np

# Counts number of times string 'name' comes up in 'list'
def count_wins(name, list):
    counter = list.count(name)
    return counter


# User must put in exact name of team in format from list. ex: "New York Yankees"
winnerCheck = input("What team do you want to check: ")

try:
    # Opens .txt file as variable 'winnerFile' and closes once outside the scope of 'with open'
    with open('WorldSeriesWinners.txt') as winnerFile:
            winnerArray = np.genfromtxt(winnerFile, delimiter= '\n', dtype=str)  # using numpy to easily read in file as array
        winnerList = winnerArray.tolist()  # convert numpy array to python list

        print("According to my records, this team has won %d times." % count_wins(winnerCheck, winnerList))


except IOError:  # If no file, print statement
    print("Excuse me adventurer, some gnolls stole my records. Could you please find them for me?")
except IndexError:  # If somehow goes outside bounds of list, print error.
    print("Sorry, there was an error with the program. Please try again.")
