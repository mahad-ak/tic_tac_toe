# Python Tic-Tac-Toe

# This is the tic tac toe game board made using a dictionary in which they keys represent the board slots
# and the corresponding values contain either the slot number or the player symbol (X, O). 
game_board = {'slot1': '1' , 'slot2': '2' , 'slot3': '3' ,
            'slot4': '4' , 'slot5': '5' , 'slot6': '6' ,
            'slot7': '7' , 'slot8': '8' , 'slot9': '9' }


# This function operates the game
def tic_tac_toe():

    # The game is started by player 'X'
    player = 'X' 
    total_turns=9 #The total number of possible turns in tic tac toe 9.

    # This counts the number of successful turns.
    turns_completed=0

    for i in range(total_turns):
        # Prints the game board so the available and filled spaces are visible to each player at each turn
        show_tic_tac_toe(game_board)

        # Prompts the player for input to add their symbol on the game board
        print("\n\nIt is player " + player + "'s turn. Which slot would you like to insert " + player + " at?")
        
        check_move(player, game_board)
        turns_completed=turns_completed+1       


# This function checks if a player's move passed in as input is a legal move and executes it, otherwise prints an error message and re-prompts the user.
def check_move(player, game_board):
        position = input()
        print("")
        
        # Adds the player's symbol to the inputted position if there is no other symbol present on that position
        if ((game_board[str("slot"+position)] == position) and (str(game_board[str("slot"+position)]) != 'X' or str(game_board[str("slot"+position)]) != 'O')):
            game_board["slot" + position] = player
        else:
            # Prints an error message and prompts the user to insert their input again
            show_tic_tac_toe(game_board)
            print("\nSorry, this slot is already filled. Which other slot would you like to insert " + player + " at?")
            check_move(player, game_board)
            return


# Prints the game board
def show_tic_tac_toe(game_board):
    return 1;

if __name__ == "__main__":
    tic_tac_toe()