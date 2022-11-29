# ----- Global Variables ------

# game board 
board = ["-", "-", "-",
        "-", "-", "-", 
        "-", "-", "-"]

# If game is still going 
game_still_going = True


# who won? or tie? 
winner = None

# whos turn is it or
current_player = "X"

# Displaying the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# game's logic in here
def play_game():

    # Display initial board
    display_board()

    # this while loop is for checking if the game is over or not 
    while game_still_going:
        
        # Turns players line 33
        handle_turn(current_player)

        # checking if game is over or not line 43.  
        check_if_game_over()

        # changing player 
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# handle a single turn (input)
def handle_turn(player):

    # who is the player 
    print(player + "'s turn")
    # entering the position
    position = input("CHoose a position from 1-9: ")

    # In here, in a while loop we are handling the input loop. 
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Python starts form 0, so, position -1 gives us the correct positioning
        position = int(position) - 1

        # IN here, we are trying to block resigning x or o over again 
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there buddy! GO again!")

        board[position] = player

    display_board()

def check_if_game_over():
    # line 48
    check_for_winner()
    # line 56 
    check_if_tie()

def check_for_winner():


    # Set up for global winner in line 13
    global winner

    # checks rows
    row_winner = check_rows()
    # checks columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there is a winner
        winner = row_winner
    elif column_winner:
        # there is a winner
        winner = column_winner
    elif diagonal_winner:
        # there is a winner
        winner = diagonal_winner
    else:
        winner = None

    return

# check for winner defs 
def check_rows():
    # Set up glabal variables
    global game_still_going
    # check if any of tje rows have all the same value - and not empty 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a winner
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return



def check_columns():
    # set up global variables
    global game_still_going

    # 
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return



def check_diagonals():
    # Set up glabal variables
    global game_still_going
    # check if any of tje rows have all the same value - and not empty 
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    

    # If any row does have a match, flag that there is a winner
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return the winner 
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
   
    return
    
    return



def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return 


def flip_player():
    # set up global variables
    global current_player
    # Changes players
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()