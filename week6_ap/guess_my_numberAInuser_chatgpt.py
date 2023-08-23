import random
from enum import Enum

class GuessResponse(Enum):
    HIGHER = "higher"
    LOWER = "lower"
    BINGO = "bingo"

def gen_random_num(n):
    return random.randint(1, n)

def guess_num(guess, num):
    if guess < num:
        return GuessResponse.HIGHER
    elif guess > num:
        return GuessResponse.LOWER
    else:
        return GuessResponse.BINGO


def ai_guess(low, high):
    return random.randint(low, high)


def play():
    max_number = int(input("Enter the maximum number for the game: "))
    num = gen_random_num(max_number)
    tries = 0
    low = 1
    high = max_number

    print(f"Guess a number between {low} and {high}.")

    while True:
        guess = int(input(f"Guess ({low}-{high}): "))
        tries += 1

        result = guess_num(guess, num)
        if result == GuessResponse.BINGO:
            print("Congratulations! You guessed the correct number.")
            break
        elif result == GuessResponse.HIGHER:
            print("Try guessing a higher number.")
            low = guess + 1
        elif result == GuessResponse.LOWER:
            print("Try guessing a lower number.")
            high = guess - 1
        else:
            print("Invalid input. Please enter a number.")

        # AI's turn
        ai_guess_num = ai_guess(low, high)
        print(f"The AI guesses {ai_guess_num}.")
        ai_result = guess_num(ai_guess_num, num)
        if ai_result == GuessResponse.BINGO:
            print("AI wins!")
            break

    print(f"It took AI {tries} tries to guess the number {num}.")


if __name__ == "__main__":
    play()