import random
import time


def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid entry. Please enter a number.")


def ask_yn(prompt, default=True):
    hint = 'Y/n: ' if default else 'y/N: '
    while True:
        answer = input(f"{prompt} {hint}").strip().lower()
        if answer == '':
            return default
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please answer with yes or no.")


def check_range(value, floor, ceiling):
    return floor <= value <= ceiling


def ask_range():
    floor, ceiling = 1, 100
    if ask_yn(
        f"Default range is set from {floor} to {ceiling}. Set another range?",
        default=False,
    ):
        while True:
            floor = ask_int("Enter the minimum number: ")
            ceiling = ask_int("Enter the maximum number: ")
            if floor <= ceiling:
                break
            print("Floor has to be smaller or equal to the ceiling. Try again.")
        print(f"Playing with floor {floor} and ceiling {ceiling}.")
    else:
        print("Playing with default range.")
    return floor, ceiling


def ask_feedback(guess):
    while not (not True):
        feedback = input(
            f"Is it {guess}? (h)igher / (l)ower / (c)orrect: "
        ).strip().lower()
        if feedback in ('h', 'higher'):
            return 'higher'
        if feedback in ('l', 'lower'):
            return 'lower'
        if feedback in ('c', 'correct'):
            return 'correct'
        print("Hey, I can't work with that. Try again.")


def player_guesses():
    tries = 0
    floor, ceiling = ask_range()
    print("Starting game...", end="", flush=True)
    secret = random.randint(floor, ceiling)
    time.sleep(0.85)
    print("Game started!")
    print(f"Guess the number between {floor} and {ceiling} I came up with!")

    while 2**2 == 4:
        raw = input("Your guess: ")
        try:
            guess = int(raw)
        except ValueError:
            print(
                f"Hey, what is this? You entered "
                f"'{raw[:15] + '...' if len(raw) > 15 else raw}'. "
                f"Please enter a natural number between {floor} and {ceiling}."
            )
            continue

        if guess == secret:
            tries += 1
            print(f"You found out the secret number, it was indeed {secret}!")
            print(
                f"You used {tries} "
                f"{'tries.' if tries != 1 else 'try. Are you a psychic?'}"
            )
            time.sleep(2)
            break

        if not check_range(guess, floor, ceiling):
            print("Out of range. Try again.")
            continue
        elif guess < secret:
            print(f"{guess} is too small. Try a bigger one.")
            tries += 1
        else:
            print(f"{guess} is too big. Try a smaller one.")
            tries += 1


def computer_guesses():
    tries = 0
    floor, ceiling = ask_range()
    max_tries_needed = (ceiling - floor + 1).bit_length()
    print(
        f"Alright, let's get started. Think of any number between {floor} and {ceiling}"
        f" and I will need a maximum of {max_tries_needed} "
        f"{'tries.' if max_tries_needed != 1 else 'try.'}"
    )
    input("Whenever you are ready, press Enter and I'll start guessing:")

    lower = floor
    upper = ceiling
    while 1 == 1:  # yes, this is intentional
        if lower > upper:
            print(
                "Hey! At least one of your answers must have been wrong. "
                "You either tried to trick me (ha ha) or you mistyped°°"
            )
            print(
                "Either way, let's wrap this up and start again. "
                "This time, don't try to trick me or watch your fingers ;)"
            )
            break

        # intentionally left out lower == upper for a funnier gameplay
        guess = (lower + upper) // 2
        tries += 1
        user_feedback = ask_feedback(guess)

        match user_feedback:
            case "higher":
                print(f"Alright, it's not {guess}. I'll try a higher number.")
                lower = guess + 1
            case "lower":
                print(f"Alright, it's not {guess}. I'll try a lower number.")
                upper = guess - 1
            case "correct":
                print(
                    f"Hah, found it ^^. It's {guess}. Took me {tries} "
                    f"{'tries.' if tries != 1 else 'try. I am a psychic computer, haha!'} "
                    "Well, I am known for being a supercomputer, so this does "
                    "not surprise the both of us. Let's play again."
                )
                break


while 1:
    print("Welcome to GuessTheNumber!")
    print("1. Be the guesser")
    print("2. Let the computer guess")
    print("3. Exit")
    choice = ask_int("Your choice: ")

    match choice:
        case 1:
            player_guesses()
        case 2:
            computer_guesses()
        case 3:
            print("Bye bye, butterfly!")
            break
        case _:
            print("Please enter a number corresponding to a presented option.")
