###########
#
#  Classroom Lookup
#  Author: Mose Butler
#  Version: 1.0.0
#  Date: 12/09/18
#
###########

# Create Dictionaries based on class assignment
roomDictionary = {"CS101": "3004",
                  "CS102": "4501",
                  "CS103": "6755",
                  "NT110": "1244",
                  "CM241": "1411"}
instructorDictionary = {"CS101": "Haynes",
                        "CS102": "Alvarado",
                        "CS103": "Rich",
                        "NT110": "Burke",
                        "CM241": "Lee"}
timeDictionary = {"CS101": "8:00 AM",
                  "CS102": "9:00 AM",
                  "CS103": "10:00 AM",
                  "NT110": "11:00 AM",
                  "CM241": "11:00 PM"}

# User declared variable
key = input("What class would you like information on: ")

# Prints values based associated with users class lookup in dictionaries.
try:
    print("Class: %s \n"
      "Room Number: %s \n"
      "Instructor: %s \n"
      "Time: %s " % (key, roomDictionary[key], instructorDictionary[key], timeDictionary[key]))
# If not in dictionaries display this message
except KeyError:
    print("\nInvalid Entry. Please restart program and enter a valid course number.")