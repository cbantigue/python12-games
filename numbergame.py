import random 

def guess(x):
    randomnumber = random.randint(1, x)
    guess = 0 
    while guess != randomnumber:
        guess = int(input(f"Guess a number from 1 and {x}: "))
        if guess < randomnumber:
            print("Sorry, the number guessed is too low. ")
        elif guess > randomnumber:
            print("Sorry, number guessed is too high, Guess again. ")
    print (f"Awesome! You guessed the number {randomnumber} correctly. ")
guess(10)

def computerguess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), or too low (L) or correct (C)?').lowercase
        if feedback == 'h': 
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print ('Yay the computer guessed your number, {guess}, correctly! ')

while True:
    gameoption = input("Press 1 to play guess, 2 to play computer guess, or Q to quit: ").lowecase
    if gameoption == 'guess':
        guess()
    elif gameoption == 'computerguess':
        computerguess()
    elif gameoption == 'q':
        quit 
        break 