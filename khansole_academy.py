"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

ANSWERS_FOR_MASTERY = 3
RANDOM_NUM_LOWER_BOUND = 10
RANDOM_NUM_UPPER_BOUND = 99

def main():
    correct_answers = 0
    while correct_answers < ANSWERS_FOR_MASTERY:
        random_int_1 = random.randint(RANDOM_NUM_LOWER_BOUND, RANDOM_NUM_UPPER_BOUND)
        random_int_2 = random.randint(RANDOM_NUM_LOWER_BOUND, RANDOM_NUM_UPPER_BOUND)
        print("What is " + str(random_int_1) + " + " + str(random_int_2) + "?")
        sum_of_ints = random_int_1 + random_int_2
        user_answer = int(input("Your answer:"))
        if sum_of_ints == user_answer:
            correct_answers +=1
            print("Correct! You've gotten " + str(correct_answers) + " in a row")
        else:
            correct_answers = 0
            print("Incorrect. The expected answer is " + str(sum_of_ints) + ".")
    print ("Congratulations! You mastered addition")
    pass

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
