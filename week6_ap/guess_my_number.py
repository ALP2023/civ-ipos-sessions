import random
MAX_NUMBER = 100

def gen_random_num(n):
    return random.randint(1, n+1)

def guess_num(guess, num):
    return('higher', 'lower', 'bingo')

def play():
    num = gen_random_num(MAX_NUMBER)
    tries = 0
    while True:
        print(f"Guess a number between 1 and {MAX NUMBER}")
    guess = int(input('Guess> '))
    tries +=1
    if guess_num(guess,num) == 'bingo':
        break

    print("You guessed right!")
    print(f"It took you {tries}")

