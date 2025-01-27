import random


def starting_message():
    # Print a rounds starting message to the user
    print("I'm thinking of a number between 0 and 100...")


def exit_message():
    # Print an exit message to the user
    print("Thank you for playing. Good bye!")


def round_end_message(num):
    # Print a message at the end of a round showing number of guesses
    print(f"This round was completed in {num} guesses.")


def play_again_loop():
    # Determine if the user wishes to play again or exit
    while True:
        ans = input("Do you want to play again? Please type 'Yes' or 'No': ").lower().strip()
        if ans in ['yes', 'ye', 'yeah', 'ok', 'go on then']:
            return True
        elif ans in ['no', 'bye', 'quit', 'exit']:
            return False
        else:
            print("I'm not sure what you meant.")


def input_validation_check_for_int(input_value):
    # Checks whether an input value is castable as an int
    try:
        i = int(input_value)
    except ValueError:
        print("You did not enter a valid number. Try again.")
        return None
    else:
        return i


def respond_to_guess(guess, num):
    # Responds to the users guesses, answering higher, lower or a winning message
    if num > guess:
        print(f"The number i'm thinking of is greater than {guess}.")
        return False
    elif num < guess:
        print(f"The number i'm thinking of is smaller than {guess}.")
        return False
    elif num == guess:
        print(f"Well done, that's correct! I was thinking of {num}. You won!")
        return True


def play_game_round():
    # Initialises a rounds starting values and begins the round game loop
    starting_message()
    secret_number = random.randint(0, 100)
    num_guesses = 0
    previous_guesses = set()
    while True:
        user_guess = input_validation_check_for_int(input())
        if user_guess and user_guess not in previous_guesses:
            previous_guesses.add(user_guess)
            num_guesses += 1
            if respond_to_guess(user_guess, secret_number):
                break
        else:
            print("You already guessed that number.")
    round_end_message(num_guesses)


def game_loop():
    # The main loop of the game
    while True:
        play_game_round()
        if not play_again_loop():
            break

    exit_message()


def main():
    game_loop()


if __name__ == "__main__":
    main()
