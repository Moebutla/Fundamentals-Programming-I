####
#   Prime Calculator
#   Author: Mose Butler
#   Date: 10/13/18
#   Version: 1.0.0
####

from math import *


def is_prime(primecheck):
    if primecheck == 2 or primecheck == 3:  # 2 and 3 are prime numbers, returns true.
        return True
    elif primecheck % 2 == 0:  # if even, not prime
        return False
    else:
        for iteration in range(3, int(sqrt(primecheck))+1, 2):
            if primecheck % iteration == 0:
                return False
        return True


number = int(input("Input a positive number to test if it is prime: "))

if is_prime(number):
    print("Your number is prime!")
else:
    print("Your number is not prime.")
