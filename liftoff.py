"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

COUNTDOWN = 10 #This constant defines the number of seconds to countdown from

"""
This function works by using a for loop to iterate down as we count. To use this, we use the constant we defined
to create a counter within our function. this counter is then printed through on every iteration of the for loop. After
printing we subtract to "count down". At the end of the function we print "Lift off"

Note the way we structured our function we do not print a 0.
"""

def main():
    counter = COUNTDOWN
    for i in range (COUNTDOWN):
        print(str(counter))
        counter -=1
    print("Liftoff!")
    pass

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
