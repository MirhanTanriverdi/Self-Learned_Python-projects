import random

def play():
    user = input("'r' for rock, 'p', for paper, 's' for scissors\n > ")
    computer = random.choice(['r', 'p', 's'])
    print("> ", computer)

    # game logic
    # r > s, s > p, p > r

    if user == computer:
        return 'It\'s a tie'
    elif is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'

    

def is_win(player, oppenent):
    # returns true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p') or (player == 'p' and oppenent == 'r'):
        return True

print(play())