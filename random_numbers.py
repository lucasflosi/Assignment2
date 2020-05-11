"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

MIN_RANDOM = 0
#Lower bound of range for us to generate random numbers
MAX_RANDOM = 100
#Upper bound of range for us to generate random numbers
NUM_RANDOM = 10
# the number of random numbers we want to print

"""
This is a simple program that generates random numbers based on the variables defined in the
3 constants above. The first constant, min_random is the lower bound for the random number generate
where as max_random is the upper bound. Num_random tells us how many numbers to generate.

In the body of the function we define a counter. We use this counter to ensure that our
while loop iterates through the correct number of times. Inside the while loop we generate and print out a random number
Once we have printed a number we add 1 to the counter. The while loop operates as long as counter is LESS than num random. 
Since we add to the counter after printing a random number, there is no fencepost error

"""

def main():
    counter = 0
    while counter < NUM_RANDOM:
        print(random.randint(MIN_RANDOM,MAX_RANDOM))
        counter += 1


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
