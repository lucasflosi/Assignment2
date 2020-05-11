"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""
import math

def main():
    user_number = input("Enter a number: ")
    print(type(user_number))
    print(user_number.isdigit())
    check_input(user_number)
    print("fail")

    while inputisinvalid:

    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    pass


def check_input(user_entered_num):
    while type(user_entered_num) != int:
        print("C")
        try:
            user_entered_num = int(user_entered_num)
            print("a")
        except ValueError:
            user_entered_num = int(input("Please enter a whole number integer: "))
            print(type(user_entered_num))
            print("w")
    return user_entered_num






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
