import random

def game(a):
    level = {1: 10, 2: 100, 3: 1000, 4: 10000, 5: 100000}
    b = random.randint(1, level[a])
    count = 0

    while True:
        c = int(input("Enter ur guess: "))

        if c > b:
            print(f"Your guess {c} is too high")
            count += 1
            continue

        elif c < b:
            print(f"Your guess {c} is too low")
            count += 1
            continue

        elif c == b:
            count += 1
            print(f"You won !!!".center(100))
            print(f"It took {count} turns to guess".center(100))
            nums = int(input("\n1 for playing again , 0 for exiting: "))

            if nums == 1:
                gaming()
            else:
                break


def gaming():
    try:
        a = int(input("Enter choice for setting difficulty (1,2,3,4,5): "))

        if a not in [1, 2, 3, 4, 5]:
            raise ValueError

    except ValueError:
        print("Invalid choice defaulting to easy")
        a = 1

    game(a)


print("Welcome to number guessing game !!!".center(100))
print("\nChoose Game Difficulty:\n1)Easy \n2)Normal \n3)Hard \n4)Super hard \n5)Impossible")
gaming()
