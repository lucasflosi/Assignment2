"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    subtract_numbers()
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    pass

def subtract_numbers():
    print("This program subtracts one number from another.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3= num1-num2
    print ("The result is " + str(num3))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()