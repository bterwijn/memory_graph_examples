print("    NOTE: ZOMBIES ATTACKED YOUR SCHOOL! RUN TO THE ROOF TOP OF THE SCHOOL TO SURVIVE!")
print("-- IMPORTANT INFORMATIONS:\n == ROOF   -5TH FLOOR \n == HEALTH -100\n == ENERGY -100 \n == FOOD  -2")
HEALTH = 100
food = 2
ENERGY = 100
FLOOR = 1

MENU = (
    "1) SEARCH CLASSROOM",
    "2) EAT FOOD",
    "3) REST",
    "4) CLIMB UPSTAIRS",
    "5) VIEW STATUS",
    "6) QUIT"
)

search_classroom = [
    "1) FOOD FOUND",
    "2) ZOMBIE ATTACK",
    "3) FOUND NOTHING"
]

while True:
    print("\nMENU:")
    for items in MENU:
        print(items)

    work = int(input("What do you want to do? : "))

    if work == 1:
        for outcomes in search_classroom:
            print(outcomes)

        dam = int(input("What happened? : "))

        if dam == 1:
            food = food + 1
            ENERGY = ENERGY - 10
            print(f"CURRENT FOOD : {food}")
            print(f"CURRENT ENERGY : {ENERGY}")

        elif dam == 2:
            HEALTH = HEALTH - 25
            ENERGY = ENERGY - 15
            print(f"CURRENT HEALTH : {HEALTH}")
            print(f"CURRENT ENERGY : {ENERGY}")

        elif dam == 3:
            ENERGY = ENERGY - 10
            print(f"CURRENT ENERGY : {ENERGY}")

        else:
            print("INVALID CHOICE!")

    elif work == 2:
        if food > 0:
            food = food - 1
            HEALTH = HEALTH + 20

            if HEALTH > 100:
                HEALTH = 100

            print(f"CURRENT FOOD : {food}")
            print(f"CURRENT HEALTH : {HEALTH}")

        else:
            print("NO FOOD LEFT!")

    elif work == 3:
        ENERGY = ENERGY + 20

        if ENERGY > 100:
            ENERGY = 100

        print(f"CURRENT ENERGY : {ENERGY}")

    elif work == 4:
        if ENERGY > 30:
            ENERGY = ENERGY - 30
            FLOOR = FLOOR + 1
            print(f"CURRENT ENERGY : {ENERGY}")
            print(f"CURRENT FLOOR : {FLOOR}")

        else:
            print("TOO TIRED TO CLIMB UPSTAIRS!")

    elif work == 5:
        print(f"HEALTH : {HEALTH}")
        print(f"ENERGY : {ENERGY}")
        print(f"FOOD : {food}")
        print(f"FLOOR : {FLOOR}")

    elif work == 6:
        print("GAME OVER!")
        break

    else:
        print("INVALID MENU CHOICE!")

    if HEALTH <= 0 or ENERGY <= 0:
        print("GAME OVER! ZOMBIES KILLED YOU!")
        break

    if FLOOR == 5:
        print("DO YOU HEAR SCREAMS FROM BELOW? RUN FAST TO THE ROOF TOP!!")

    if FLOOR >= 5:
        print("\nYOU WON! YOU SURVIVED THE ZOMBIE ATTACK!")
        break
