import random



class Characters:
    num_of_chars = 0


    def __init__(self, name, level, gold):
        self.name = name
        self.level = level
        self.gold = gold


        Characters.num_of_chars += 1



class Mage(Characters):
    spell_type = "fire"



class Assassin(Characters):
    spell_type = "shadow"



character1 = Mage("Aria", 3, 100)
character2 = Assassin("Dren", 5, 80)
character3 = Mage("Kael", 4, 120)
character4 = Assassin("Vex", 2, 60)
character_list = [character1, character2, character3, character4]



def view_guild_members(characters):
    print("Members currently in the guild:")
    for character in characters:
        print(f"{character.name}, level {character.level}, Gold {character.gold}")
    print()


    go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()
    while True:
        if go_back == "Y":
            return characters
        else:
            go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()



def train_character(characters, character_names):
    print("Training costs 10 gold. \nAvailable characters to train: ")
    for character in characters:
        if character.gold >= 10:
            print(f"{character.name}, level {character.level}")


    training_cost = 10


    while True:
        train_character = input("Which character do you want to train (Exit to go back): ").capitalize()
        print()


        if train_character == "Exit":
            break
        while train_character not in (character_names):
            train_character = input("That is not a valid character. Choose a valid character or 'Exit' to exit: ").capitalize()
            print()


        for character in characters:
            if train_character == character.name:
                while character.gold >= training_cost:
                    character.gold -= 10
                    character.level += 1
                    print(f"{character.name} levelled up!")
                    print(f"{character.gold} gold remaining.")
                    print()
                    train_again = input(f"Do you want to train {character.name} again(Y/N): ").capitalize()
                    while train_again not in ("Y", "N"):
                        train_again = input("Please type Y to train again or N to cancel: ").capitalize()
                    if train_again == "Y":
                        continue
                    elif character.gold == 0:
                        print(f"You don't have enough gold left to train {character.name}.")
                        break
                    elif train_again == "N":
                        break
                    return characters, character_names


                else:
                    print(f"You don't have enough gold left to train {character.name}.")
                    print()
                    return characters, character_names
        break


    return characters, character_names



def recruit_character(characters, char_names):
    recruit_character = input("Do you want to recruit a new character (Y/N): ").capitalize()
    print()


    while recruit_character not in ("Y", "N"):
        recruit_character = input("Enter Y or N for recruting a new character: ").capitalize()


    if recruit_character == "Y":
        new_character = input("Who are you recruiting: ").capitalize()


        while new_character in char_names:
            new_character = input("This name is already taken. Please change your name to join: ")
        else:
            recruit_class = input("Which class is the new recruit (Mage or Assassin): ").capitalize()
            while recruit_class not in ("Mage", "Assassin"):
                recruit_class = input("Select if they are a Mage or Assassin: ").capitalize()


            if recruit_class == "Mage":
                characters.append(Mage(new_character, 1, 100))
                char_names.append(new_character)
                return characters, char_names, new_character
            elif recruit_class == "Assassin":
                characters.append(Assassin(new_character, 1, 100))
                char_names.append(new_character)
                return characters, char_names, new_character


    elif recruit_character == "N":
        return characters, char_names, None



def view_guild_stats(characters):
    highest_lv_char_pos = 0
    most_gold_char_pos = 0
    all_levels = []
    mage_count = 0
    assassin_count = 0
    total_gold = 0


    for character in characters:
        if character.level > highest_lv_char_pos:
            highest_lv_char_pos = character.level
            highest_lv_char = character.name


    for character in characters:
        if character.gold > most_gold_char_pos:
            most_gold_char_pos = character.gold
            most_gold_char = character.name


        total_gold += character.gold


    for character in characters:
        all_levels.append(character.level)


    average_level = sum(all_levels) / len(all_levels)


    for character in characters:
        if isinstance(character, Mage):
            mage_count += 1
        if isinstance(character, Assassin):
            assassin_count += 1


    print(f"Highest levelled character: {highest_lv_char}")
    print(f"Character with the most gold: {most_gold_char}")
    print(f"Average level in the guild: {average_level:.1f}")
    print(f"Number of mages: {mage_count}")
    print(f"Number of assassins: {assassin_count}")
    print(f"Total gold in the guild: {total_gold}")
    print()


    go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()
    while True:
        if go_back == "Y":
            return
        else:
            go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()



def tournament(characters, char_names, rounds, wins_losses, total_wins):
    print(f"Available character are: {char_names}")
    win_chance = 50
    opponent = random.choice(characters)
    player_char = input("Choose which character you will use: ").capitalize()
    print()


    while player_char not in char_names:
        player_char = input("That's not a charcter. Choose which character you will use: ").capitalize()
        print()


    for character in characters:
        if player_char == character.name:
            player_char = character


    while player_char is opponent:
        opponent = random.choice(characters)


    if player_char.level > opponent.level:
        win_chance += 10
    else:
        win_chance -= 10


    if isinstance(player_char, Assassin):
        win_chance += 10
    else:
        win_chance -= 10


    while True:
        if player_char.level < 2:
            print("This character needs to be a higher level before using it in a tournament.")
            print()
            return characters, rounds, wins_losses, total_wins
        else:
            break


    print(f"This round is {player_char.name} vs {opponent.name}")


    winner_select = random.randint(1, 100)
    if win_chance >= winner_select:
        player_char.gold += 20
        player_char.level += 1
        wins_losses[player_char.name]["Wins"] += 1
        total_wins += 1
        if opponent.gold >= 10:
            opponent.gold -= 10
        print("You won! You earned 20 gold. You gained 1 level.")
        print(f"You now have {player_char.gold} gold and are level {player_char.level}")
        print()
    else:
        if player_char.gold >= 10:
            player_char.gold -= 10
        opponent.gold += 20
        opponent.level += 1
        wins_losses[player_char.name]["Losses"] += 1
        print("You lost 10 gold. The opponent gained 20 gold and 1 level.")
        print(f"Your remaining gold is {player_char.gold}.")
        print()


    rounds += 1
    highest_wins = 0
    highest_winning_char = ""
    for name, results in wins_losses.items():
        if results["Wins"] > highest_wins:
            highest_wins = results["Wins"]
            highest_winning_char = name


    print(f"Total number of tounrmanent rounds played: {rounds}")
    print(wins_losses)
    print(f"Characters with the most wins: {highest_winning_char} with {highest_wins} wins.")
    print(f"Total wins within the guild: {total_wins}")
    print()


    return characters, rounds, wins_losses, total_wins



def main():
    characters = character_list
    char_names = [character.name for character in characters]
    rounds = 0
    total_wins = 0
    wins_losses = {character.name: {"Wins": 0, "Losses": 0} for character in characters}
    while True:
        print("Main menu")
        menu_choice = input(" (1) View guild members. \n (2) Train a character. \n (3) Recruit a new character. \n "
                            "(4) View guild's statistics \n (5) Enter a tournament. \n (6) Exit \n choose an option: ")
        print()
        match menu_choice:
            case "1":
                characters = view_guild_members(characters)
            case "2":
                characters, char_names = train_character(characters, char_names)
            case "3":
                characters, char_names, new_character = recruit_character(characters, char_names)
                char_names = [character.name for character in characters]
                if new_character != None:
                    wins_losses[new_character] = {"Wins": 0, "Losses": 0}
            case "4":
                view_guild_stats(characters)
            case "5":
                characters, rounds, results, total_wins = tournament(characters, char_names, rounds, wins_losses, total_wins)
                wins_losses = results
            case "6":
                break
            case _:
                print("That's not a valid choice.")
                continue



if __name__ == "__main__":
    while True:
        main()
        print("Bye.")
        break



class Characters:
    num_of_chars = 0


    def __init__(self, name, level, gold):
        self.name = name
        self.level = level
        self.gold = gold


        Characters.num_of_chars += 1



class Mage(Characters):
    spell_type = "fire"



class Assassin(Characters):
    spell_type = "shadow"



character1 = Mage("Aria", 3, 100)
character2 = Assassin("Dren", 5, 80)
character3 = Mage("Kael", 4, 120)
character4 = Assassin("Vex", 2, 60)
character_list = [character1, character2, character3, character4]



def view_guild_members(characters):
    print("Members currently in the guild:")
    for character in characters:
        print(f"{character.name}, level {character.level}, Gold {character.gold}")
    print()


    go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()
    while True:
        if go_back == "Y":
            return characters
        else:
            go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()



def train_character(characters, character_names):
    print("Training costs 10 gold. \nAvailable characters to train: ")
    for character in characters:
        if character.gold >= 10:
            print(f"{character.name}, level {character.level}")


    training_cost = 10


    while True:
        train_character = input("Which character do you want to train (Exit to go back): ").capitalize()
        print()


        if train_character == "Exit":
            break
        while train_character not in (character_names):
            train_character = input("That is not a valid character. Choose a valid character or 'Exit' to exit: ").capitalize()
            print()


        for character in characters:
            if train_character == character.name:
                while character.gold >= training_cost:
                    character.gold -= 10
                    character.level += 1
                    print(f"{character.name} levelled up!")
                    print(f"{character.gold} gold remaining.")
                    print()
                    train_again = input(f"Do you want to train {character.name} again(Y/N): ").capitalize()
                    while train_again not in ("Y", "N"):
                        train_again = input("Please type Y to train again or N to cancel: ").capitalize()
                    if train_again == "Y":
                        continue
                    elif character.gold == 0:
                        print(f"You don't have enough gold left to train {character.name}.")
                        break
                    elif train_again == "N":
                        break
                    return characters, character_names


                else:
                    print(f"You don't have enough gold left to train {character.name}.")
                    print()
                    return characters, character_names
        break


    return characters, character_names



def recruit_character(characters, char_names):
    recruit_character = input("Do you want to recruit a new character (Y/N): ").capitalize()
    print()


    while recruit_character not in ("Y", "N"):
        recruit_character = input("Enter Y or N for recruting a new character: ").capitalize()


    if recruit_character == "Y":
        new_character = input("Who are you recruiting: ").capitalize()


        while new_character in char_names:
            new_character = input("This name is already taken. Please change your name to join: ")
        else:
            recruit_class = input("Which class is the new recruit (Mage or Assassin): ").capitalize()
            while recruit_class not in ("Mage", "Assassin"):
                recruit_class = input("Select if they are a Mage or Assassin: ").capitalize()


            if recruit_class == "Mage":
                characters.append(Mage(new_character, 1, 100))
                char_names.append(new_character)
                return characters, char_names, new_character
            elif recruit_class == "Assassin":
                characters.append(Assassin(new_character, 1, 100))
                char_names.append(new_character)
                return characters, char_names, new_character


    elif recruit_character == "N":
        return characters, char_names, None



def view_guild_stats(characters):
    highest_lv_char_pos = 0
    most_gold_char_pos = 0
    all_levels = []
    mage_count = 0
    assassin_count = 0
    total_gold = 0


    for character in characters:
        if character.level > highest_lv_char_pos:
            highest_lv_char_pos = character.level
            highest_lv_char = character.name


    for character in characters:
        if character.gold > most_gold_char_pos:
            most_gold_char_pos = character.gold
            most_gold_char = character.name


        total_gold += character.gold


    for character in characters:
        all_levels.append(character.level)


    average_level = sum(all_levels) / len(all_levels)


    for character in characters:
        if isinstance(character, Mage):
            mage_count += 1
        if isinstance(character, Assassin):
            assassin_count += 1


    print(f"Highest levelled character: {highest_lv_char}")
    print(f"Character with the most gold: {most_gold_char}")
    print(f"Average level in the guild: {average_level:.1f}")
    print(f"Number of mages: {mage_count}")
    print(f"Number of assassins: {assassin_count}")
    print(f"Total gold in the guild: {total_gold}")
    print()


    go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()
    while True:
        if go_back == "Y":
            return
        else:
            go_back = input("Do you want to return to the main menu (Y/N): ").capitalize()



def tournament(characters, char_names, rounds, wins_losses, total_wins):
    print(f"Available character are: {char_names}")
    win_chance = 50
    opponent = random.choice(characters)
    player_char = input("Choose which character you will use: ").capitalize()
    print()


    while player_char not in char_names:
        player_char = input("That's not a charcter. Choose which character you will use: ").capitalize()
        print()


    for character in characters:
        if player_char == character.name:
            player_char = character


    while player_char is opponent:
        opponent = random.choice(characters)


    if player_char.level > opponent.level:
        win_chance += 10
    else:
        win_chance -= 10


    if isinstance(player_char, Assassin):
        win_chance += 10
    else:
        win_chance -= 10


    while True:
        if player_char.level < 2:
            print("This character needs to be a higher level before using it in a tournament.")
            print()
            return characters, rounds, wins_losses, total_wins
        else:
            break


    print(f"This round is {player_char.name} vs {opponent.name}")


    winner_select = random.randint(1, 100)
    if win_chance >= winner_select:
        player_char.gold += 20
        player_char.level += 1
        wins_losses[player_char.name]["Wins"] += 1
        total_wins += 1
        if opponent.gold >= 10:
            opponent.gold -= 10
        print("You won! You earned 20 gold. You gained 1 level.")
        print(f"You now have {player_char.gold} gold and are level {player_char.level}")
        print()
    else:
        if player_char.gold >= 10:
            player_char.gold -= 10
        opponent.gold += 20
        opponent.level += 1
        wins_losses[player_char.name]["Losses"] += 1
        print("You lost 10 gold. The opponent gained 20 gold and 1 level.")
        print(f"Your remaining gold is {player_char.gold}.")
        print()


    rounds += 1
    highest_wins = 0
    highest_winning_char = ""
    for name, results in wins_losses.items():
        if results["Wins"] > highest_wins:
            highest_wins = results["Wins"]
            highest_winning_char = name


    print(f"Total number of tounrmanent rounds played: {rounds}")
    print(wins_losses)
    print(f"Characters with the most wins: {highest_winning_char} with {highest_wins} wins.")
    print(f"Total wins within the guild: {total_wins}")
    print()


    return characters, rounds, wins_losses, total_wins



def main():
    characters = character_list
    char_names = [character.name for character in characters]
    rounds = 0
    total_wins = 0
    wins_losses = {character.name: {"Wins": 0, "Losses": 0} for character in characters}
    while True:
        print("Main menu")
        menu_choice = input(" (1) View guild members. \n (2) Train a character. \n (3) Recruit a new character. \n "
                            "(4) View guild's statistics \n (5) Enter a tournament. \n (6) Exit \n choose an option: ")
        print()
        match menu_choice:
            case "1":
                characters = view_guild_members(characters)
            case "2":
                characters, char_names = train_character(characters, char_names)
            case "3":
                characters, char_names, new_character = recruit_character(characters, char_names)
                char_names = [character.name for character in characters]
                if new_character != None:
                    wins_losses[new_character] = {"Wins": 0, "Losses": 0}
            case "4":
                view_guild_stats(characters)
            case "5":
                characters, rounds, results, total_wins = tournament(characters, char_names, rounds, wins_losses, total_wins)
                wins_losses = results
            case "6":
                break
            case _:
                print("That's not a valid choice.")
                continue



if __name__ == "__main__":
    while True:
        main()
        print("Bye.")
        break
