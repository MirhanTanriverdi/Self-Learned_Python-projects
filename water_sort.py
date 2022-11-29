# Green is 1 , red is 2, and 0 is the free space

# Game Board
board = ["1: ", "1", "0", "0",
        "2: ", "2", "1", "2", 
        "3: ", "2", "1", "0"]

# If game is still one 
game_still_going = True

# Displaying the board
def display_board():
    print(board[0] + board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + board[5] + " | " + board[6] + " | " + board[7])
    print(board[8] + board[9] + " | " + board[10] + " | " + board[11])

winner = None

# Game logic
def play_game():
    
    # Display inital board
    display_board()

    while game_still_going:

        # moving beaker's liquid to other
        handle_move()

        # checking game is over or not 
        check_if_game_over()
    
    
    # if every beaker is full finish the game
    if winner:
        print("You made it dudee!")
    elif winner == None:
        print("AAAAAA! Try again!")


def handle_move():
    
    # entering the position
    position_1 = input("Move beaker " )
    position_2 = input("to ")

    # Input loop
    valid = False
    while not valid:
        while position_1 and position_2 not in ["1", "2", "3"]:
            position = input("Invalid Beaker enter again! Move beaker to: ")

    # python count starts from 0, that's why
            position = int(position) - 1

    # moving liquid between beakers
            if board[position] == "0":
                valid = True
            else:
                print("Can't make that move")
    
    return


    display_board()

def beaker_move():
    
    # global variable in another def 
    global game_still_going

    beaker_1 = board[1] == board[2] == board[3] 
    beaker_2 = board[5] == board[6] == board[7]
    beaker_3 = board[9] == board[10] == board[11]

    


play_game()