import random as r

choice = ""
number = 0
attempt = ""
attempt_counter = 0
start_live = 0
lives = 0

def randomizer(choice):
    if choice == "1":
        number = r.randint(1, 10)
        start_live = 5
        return number, start_live
    elif choice == "2":
        number = r.randint(1, 50)
        start_live = 10
        return number, start_live
    elif choice == "3":
        number = r.randint(1, 100)
        start_live = 50
        return number, start_live

def vergleich(versuch):
    if attempt < number:
        print(f"Higher!")
        print(f"You have {lives} attempts left!")
        global attempt_counter
        attempt_counter += 1
    elif attempt > number:
        print(f"lower!")
        print(f"You have {lives} attempts left!")
        attempt_counter += 1

def rating():
    if attempt_counter < 0.1*start_live:
        print(f"Awesome!")
    elif attempt_counter < 0.5*start_live:
        print(f"Better luck next time!")
    else:
        print(f"That was bad!")


while True:
    choice = input(f"Chose your difficulty\n"
                   f"1) Easy(number between 1 and 10 | 5 attempts)\n"
                   f"2) Medium(number between 1 and 50 | 7 attempts)\n"
                   f"3) Hard(number between 1 and 100 | 10 attempts)\n"
                   f"4) Leave\n")
    if choice == "4":
        print(f"Goodbye!")
        break


    number, start_live = randomizer(choice)
    lives = start_live
    while True:
        attempt = input(f"Which number did i choose?\n")

        try:
            attempt = int(attempt)
        except ValueError:
            print(f"Only use numbers")
            continue

        if attempt != number and lives > 0:
            lives -= 1
            vergleich(attempt)
            continue
        elif lives <= 0:
            print(f"Out of attempts!")
            break
        else:
            print(f"Correct!\n")
            attempt_counter += 1
            print(f"You needed {attempt_counter} attempts!")
            rating()
            print()
            print()
            attempt_counter = 0
            break
