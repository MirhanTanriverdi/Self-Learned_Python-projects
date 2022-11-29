# Green is 1 , red is 2, and 0 is the free space

# define the board as matrix
board = [
    ["1", "0", "0"], # beaker 1
    ["2", "1", "2"], # beaker 2
    ["2", "1", "0"]  # beaker 3
]

# If game is still one
game_in_progress = False

# set winner
winner = None

# Displaying the board
def display_board():
    # print board in matrix
    print(f' 1: {board[0]} \n 2: {board[1]} \n 3: {board[2]}')


def check_if_game_over():
    # set beakers
    beaker_1 = board[0]
    beaker_2 = board[1]
    beaker_3 = board[2]

    # set beaker complete status
    beaker_1_complete = False
    beaker_2_complete = False
    beaker_3_complete = False

    # check if all values in the board are the same
    if beaker_1[0] == beaker_1[1] == beaker_1[2]:
        beaker_1_complete = True
    if beaker_2[0] == beaker_2[1] == beaker_2[2]:
        beaker_2_complete = True
    if beaker_3[0] == beaker_3[1] == beaker_3[2]:
        beaker_3_complete = True

    # check if all beakers are complete
    if beaker_1_complete and beaker_2_complete and beaker_3_complete:
        return True

    return False

# Game logic


def play_game():
    global game_in_progress
    global winner

    game_in_progress = True
    # add welcome message
    print("Welcome to the game of Mirhan.")
    # Display initial board
    display_board()

    while game_in_progress:
        # moving beaker's liquid to other
        status, beaker_to_move, beaker_to_pour_into = handle_move()
        if status:
            # move the liquid
            move_liquid(beaker_to_move, beaker_to_pour_into)
            # display the board
            display_board()
            # check if the game is over
            if check_if_game_over():
                # set winner to true
                winner = True
                # set game_in_progress to false
                game_in_progress = False
                # if every beaker is full finish the game
                if winner:
                    print("You made it dudee!")
                elif winner == None:
                    print("AAAAAA! Try again!")

def handle_move():
    # select beaker
    get_beaker_to_move = input("Select beaker to move: ")
    # validate the input
    while get_beaker_to_move not in ["1", "2", "3"]:
        # print error message
        print("Invalid input. Please select beaker to move again.")
        # ask again
        get_beaker_to_move = input("Select beaker to move: ")

    # convert to int
    get_beaker_to_move = int(get_beaker_to_move)
    print(f"You selected beaker - {get_beaker_to_move}")

    # select the beaker to pour liquid into
    get_beaker_to_pour_into = input("Select beaker to pour liquid into: ")
    # validate the input
    while get_beaker_to_pour_into not in ["1", "2", "3"]:
        # print error message
        print("Invalid input. Please select beaker to pour liquid into again.")
        # ask again
        get_beaker_to_pour_into = input("Select beaker to pour liquid into: ")

    # convert to int
    get_beaker_to_pour_into = int(get_beaker_to_pour_into)
    print(f"You selected beaker - {get_beaker_to_pour_into}")

    # validate the beaker to move and beaker to pour into
    if not validate_beaker_to_move_and_beaker_to_pour_into(get_beaker_to_move, get_beaker_to_pour_into):
        # return to the main function
        return False
    
    # return true and the beaker to move and the beaker to pour into
    return True, get_beaker_to_move, get_beaker_to_pour_into

# validate the beaker to move and beaker to pour into
def validate_beaker_to_move_and_beaker_to_pour_into(get_beaker_to_move, get_beaker_to_pour_into):
    # check if the beaker to pour into is the same as the beaker to move
    if get_beaker_to_move == get_beaker_to_pour_into:
        print("You can't pour into the same beaker.")
        # return false
        return False

    # check if the beaker to move is empty
    if board[get_beaker_to_move - 1][0] == "0":
        print("Beaker is already empty.")
        # return false
        return False

    # check if the beaker to pour into is full
    if board[get_beaker_to_pour_into - 1][2] != "0":
        print("Beaker is already full.")
        # return false
        return False
    # return true
    return True

# move the liquid from the beaker to the other
def move_liquid(get_beaker_to_move, get_beaker_to_pour_into):
    # pour liquid from beaker_to_move to beaker_to_pour_into
    # get the liquid from beaker_to_move
    if board[get_beaker_to_move - 1][2] != "0":
        # get the liquid from beaker_to_move
        liquid_to_pour = board[get_beaker_to_move - 1][2]
        # remove the liquid from beaker_to_move
        board[get_beaker_to_move - 1][2] = "0"
    elif board[get_beaker_to_move - 1][1] != "0":
        # get the liquid from beaker_to_move
        liquid_to_pour = board[get_beaker_to_move - 1][1]
        # remove the liquid from beaker_to_move
        board[get_beaker_to_move - 1][1] = "0"
    elif board[get_beaker_to_move - 1][0] != "0":
        # get the liquid from beaker_to_move
        liquid_to_pour = board[get_beaker_to_move - 1][0]
        # remove the liquid from beaker_to_move
        board[get_beaker_to_move - 1][0] = "0"

    # get the empty space in beaker_to_pour_into
    if board[get_beaker_to_pour_into - 1][0] == "0":
        # pour the liquid to beaker_to_pour_into
        board[get_beaker_to_pour_into - 1][0] = liquid_to_pour
    elif board[get_beaker_to_pour_into - 1][1] == "0":
        # pour the liquid to beaker_to_pour_into
        board[get_beaker_to_pour_into - 1][1] = liquid_to_pour
    elif board[get_beaker_to_pour_into - 1][2] == "0":
        # pour the liquid to beaker_to_pour_into
        board[get_beaker_to_pour_into - 1][2] = liquid_to_pour
        

play_game()