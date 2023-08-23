import random
MAX_NUMBER = 100

def gen_random_num(n):
    return random.randint(1, n+1)


def guess_num(guess, num):
    if guess < num:
        return 'higher'
    elif guess > num:
        return 'lower'
    else:
        return 'bingo'

def play():
    num = gen_random_num(MAX_NUMBER)
    tries = 0
    low = 1
    high = MAX_NUMBER

    print(f"Guess a number between {low} and {high}.")

    while True:
        guess = int(input(f"Guess ({low}-{high}): "))
        tries += 1

        result = guess_num(guess, num)
        if result == 'bingo':
            print("Congratulations! You guessed the correct number.")
            break
        elif result == 'higher':
            print("Try guessing a higher number.")
            low = guess + 1
        elif result == 'lower':
            print("Try guessing a lower number.")
            high = guess - 1
        else:
            print("Invalid response. Please enter 'higher', 'lower', or 'bingo'.")

    print("You guessed right!")
    print(f"It took you {tries} tries.")


if __name__ == "__main__":
    play()
