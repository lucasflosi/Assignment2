"""
File: nimm.py
-------------------------
Nimm is a 2 player game where a player can remove either 1 or 2 stones. The player who removes the
last stone loses the game!
"""

STONES_IN_GAME = 20 #starting quantity for stones

def main():
    stones_left = STONES_IN_GAME
    player_turn = 1
    while stones_left > 0:
        if stones_left != STONES_IN_GAME:
            print("") #prints a blank on turns after the first turn
        print("There are " + str(stones_left) + " stones left")
        stones_removed = int(input("Player " + str(player_turn) +" would you like to remove 1 or 2 stones? "))
        while input_is_invalid(stones_removed) == False:
            stones_removed = int(input("Please enter 1 or 2: "))
        while taking_more_stones_than_exists(stones_left,stones_removed) == True:
            print("There is only 1 stone left. You cannot remove 2 stones")
            stones_removed = int(input("Player " + str(player_turn) +" would you like to remove 1 or 2 stones? "))
        stones_left -= stones_removed
        player_turn = switch_player(player_turn)
    print("")
    print("Player " + str(player_turn) + " wins!")

def input_is_invalid(user_turn):
    if user_turn == 1 or user_turn == 2:
        return True
    else:
        return False

def taking_more_stones_than_exists(num_stones_left,stones_user_wants_to_remove):
    if num_stones_left < stones_user_wants_to_remove:
        return True
    else:
        return False

def switch_player(player_turn):
    if player_turn == 1:
        new_player_turn = 2
    if player_turn == 2:
        new_player_turn = 1
    return new_player_turn

"""
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
"""

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
