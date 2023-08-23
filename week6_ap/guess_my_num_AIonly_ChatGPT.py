import random


def gen_random_num(n):
    return random.randint(1, n)


def ai_guess(low, high):
    return random.randint(low, high)


def play():
    max_number = int(input("Enter the maximum number for the game: "))
    num = gen_random_num(max_number)
    tries = 0
    low = 1
    high = max_number

    print(f"The secret number is {num}.")

    while True:
        ai_guess_num = ai_guess(low, high)
        tries += 1
        print(f"The AI guesses {ai_guess_num}.")

        if ai_guess_num == num:
            print("AI wins!")
            break
        elif ai_guess_num < num:
            print("AI guesses lower.")
            low = ai_guess_num + 1
        else:
            print("AI guesses higher.")
            high = ai_guess_num - 1

    print(f"The AI took {tries} tries to guess the number {num}.")


if __name__ == "__main__":
    play()
