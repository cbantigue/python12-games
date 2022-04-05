import random 
def play():
    user = input("Pick a weapon: 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard, or 'sp' for spock")
    computer = random.choice(['r', 'p', 's', 'l', 'sp'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent): 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'l' and opponent == 'sp') or (player == 'l' and opponent == 'p') or (player == 'r' and opponent == 'l') or (player == 'p' and opponent == 'sp') or (player == 's' and opponent == 'l') or (player == 'sp' and opponent == 's') or (player == 'sp' and opponent == 'r'): 
        return True 

