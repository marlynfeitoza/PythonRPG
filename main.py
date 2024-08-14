import time
import os
from random import randint
import random

name_monsters = ["goblin", "orc", "troll", "dragon", "giant",
                 "skeleton", "zombie", "vampire", "werewolf", "ghost"]

monsters = []

potion = 2

player = {"name": "name",
          "level": 1,
          "attack": 30,
          "health": 100,
          "max_health": 100,
          "exp": 0,
          "max_exp": 30,
          "gold": 10,
          "items": [],
          }

dungeon = False
florest = False
cave = False

sword = {"sword": 1.25, "state": False}
axe = {"axe": 1.5, "state": False}
mace = {"mace": 1.75, "state": False}
dagger = {"dagger": 1.25, "state": False}
spear = {"spear": 1.5, "state": False}
bow = {"bow": 1.75, "state": False}
crossbow = {"crossbow": 2, "state": False}
staff = {"staff": 1.5, "state": False}
wand = {"wand": 1.25, "state": False}
shield = {"shield": 1.25, "state": False}
items = ["sword", "axe", "mace", "dagger", "spear",
         "bow", "crossbow", "staff", "wand", "shield"]


def weapons_off():
    global sword
    global axe
    global mace
    global dagger
    global spear
    global bow
    global crossbow
    global staff
    global wand
    global shield
    sword = {"state": False}
    axe = {"state": False}
    mace = {"state": False}
    dagger = {"state": False}
    spear = {"state": False}
    bow = {"state": False}
    crossbow = {"state": False}
    staff = {"state": False}
    wand = {"state": False}
    shield = {"state": False}


def drop_gold():
    gold = randint(1, 10)
    player["gold"] += gold
    print(f"{player['name']} gained {gold} gold")
    draw()
    time.sleep(1)


def potion_use():
    player["health"] += 20
    if player["health"] > player["max_health"]:
        player["health"] = player["max_health"]
    print(f"{player['name']} used a potion")
    draw()
    time.sleep(1)


def inventory():
    global items
    global potion
    os.system("clear")
    draw()
    print("\t   Inventory")
    draw()
    print(f"< potion - {potion}")
    print("< gold -", player["gold"])
    for i in range(len(items)):
        draw()
        print(f"{i + 1}. {items[i]}")
    draw()
    print("equip - to equip items")
    print("unequip - to unequip items")
    print("< back - to go back")
    draw()
    choice = input("> ")
    for i in range(len(items)):
        if choice == f"equip {items[i]}":
            equip(items[i])
            break
        elif choice == f"unequip {items[i]}":
            unequip(items[i])
            break
        if choice == "back":
            draw()
            print("You went back")
            draw()
            input("Press enter to continue")
            break
    if choice == "back":
        pass
    else:
        inventory()


def unequip(item):
    global items
    global player
    global sword
    global axe
    global mace
    global dagger
    global spear
    global bow
    global crossbow
    global staff
    global wand
    global shield
    if item == "sword":
        player["attack"] /= sword["sword"]
        sword["state"] = False
    elif item == "axe":
        player["attack"] /= axe["axe"]
        axe["state"] = False
    elif item == "mace":
        player["attack"] /= mace["mace"]
        mace["state"] = False
    elif item == "dagger":
        player["attack"] /= dagger["dagger"]
        dagger["state"] = False
    elif item == "spear":
        player["attack"] /= spear["spear"]
        spear["state"] = False
    elif item == "bow":
        player["attack"] /= bow["bow"]
        bow["state"] = False
    elif item == "crossbow":
        player["attack"] /= crossbow["crossbow"]
        crossbow["state"] = False
    elif item == "staff":
        player["attack"] /= staff["staff"]
        staff["state"] = False
    elif item == "wand":
        player["attack"] /= wand["wand"]
        wand["state"] = False
    elif item == "shield":
        player["attack"] /= shield["shield"]
        shield["state"] = False
    items.append(item)
    print(f"{player['name']} unequipped {item}")
    draw()


def equip(item):
    global items
    global player
    global sword
    global axe
    global mace
    global dagger
    global spear
    global bow
    global crossbow
    global staff
    global wand
    global shield
    if item == "sword":
        player["attack"] *= sword["sword"]
        weapons_off()
        sword["state"] = True
    elif item == "axe":
        player["attack"] *= axe["axe"]
        weapons_off()
        axe["state"] = True
    elif item == "mace":
        player["attack"] *= mace["mace"]
        weapons_off()
        mace["state"] = True
    elif item == "dagger":
        player["attack"] *= dagger["dagger"]
        weapons_off()
        dagger["state"] = True
    elif item == "spear":
        player["attack"] *= spear["spear"]
        weapons_off()
        spear["state"] = True
    elif item == "bow":
        player["attack"] *= bow["bow"]
        weapons_off()
        bow["state"] = True
    elif item == "crossbow":
        player["attack"] *= crossbow["crossbow"]
        weapons_off()
        crossbow["state"] = True
    elif item == "staff":
        player["attack"] *= staff["staff"]
        weapons_off()
        staff["state"] = True
    elif item == "wand":
        player["attack"] *= wand["wand"]
        weapons_off()
        wand["state"] = True
    elif item == "shield":
        player["attack"] *= shield["shield"]
        weapons_off()
        shield["state"] = True
    items.remove(item)
    print(f"{player['name']} equipped {item}")
    draw()


def loja():
    global player
    global items
    global sword
    global potion
    print("Welcome to the shop")
    print("You have", player["gold"], "gold")
    print("0. Potion - 5 gold")
    print("1. Sword - 10 gold")
    print("2. Axe - 15 gold")
    print("3. Mace - 20 gold")
    print("4. Dagger - 5 gold")
    print("5. Spear - 10 gold")
    print("6. Bow - 15 gold")
    print("7. Crossbow - 20 gold")
    print("8. Staff - 10 gold")
    print("9. Wand - 5 gold")
    print("10. Shield - 5 gold")
    print("< back - to go back")
    choice = input("Enter your choice: ")
    if choice == "0":
        if player["gold"] >= 5:
            player["gold"] -= 5
            potion += 1
            print("You bought a potion")
        else:
            print("You don't have enough gold")
    if choice == "1":
        if player["gold"] >= 10:
            player["gold"] -= 10
            items.append("sword")
            print("You bought a sword")
        else:
            print("You don't have enough gold")
    elif choice == "2":
        if player["gold"] >= 15:
            player["gold"] -= 15
            items.append("axe")
            print("You bought an axe")
        else:
            print("You don't have enough gold")
    elif choice == "3":
        if player["gold"] >= 20:
            player["gold"] -= 20
            items.append("mace")
            print("You bought a mace")
        else:
            print("You don't have enough gold")
    elif choice == "4":
        if player["gold"] >= 5:
            player["gold"] -= 5
            items.append("dagger")
            print("You bought a dagger")
        else:
            print("You don't have enough gold")
    elif choice == "5":
        if player["gold"] >= 10:
            player["gold"] -= 10
            items.append("spear")
            print("You bought a spear")
        else:
            print("You don't have enough gold")
    elif choice == "6":
        if player["gold"] >= 15:
            player["gold"] -= 15
            items.append("bow")
            print("You bought a bow")
        else:
            print("You don't have enough gold")
    elif choice == "7":
        if player["gold"] >= 20:
            player["gold"] -= 20
            items.append("crossbow")
            print("You bought a crossbow")
        else:
            print("You don't have enough gold")
    elif choice == "8":
        if player["gold"] >= 10:
            player["gold"] -= 10
            items.append("staff")
            print("You bought a staff")
        else:
            print("You don't have enough gold")
    elif choice == "9":
        if player["gold"] >= 5:
            player["gold"] -= 5
            items.append("wand")
            print("You bought a wand")
        else:
            print("You don't have enough gold")
    elif choice == "10":
        if player["gold"] >= 5:
            player["gold"] -= 5
            items.append("shield")
            print("You bought a shield")
        else:
            print("You don't have enough gold")
    elif choice == "<":
        pass
    input("Press enter to continue")


def save_game():
    global player
    global dungeon
    global florest
    global cave
    global potion
    global items
    global monsters
    with open("save.txt", "w") as file:
        file.write(player["name"] + "\n")
        file.write(str(player["level"]) + "\n")
        file.write(str(player["attack"]) + "\n")
        file.write(str(player["health"]) + "\n")
        file.write(str(player["max_health"]) + "\n")
        file.write(str(player["exp"]) + "\n")
        file.write(str(player["max_exp"]) + "\n")
        file.write(str(dungeon) + "\n")
        file.write(str(florest) + "\n")
        file.write(str(cave) + "\n")
        file.write(str(potion) + "\n")
        file.write(str(len(items)) + "\n")
        for item in items:
            file.write(item + "\n")
        for monster in monsters:
            file.write(monster["name"] + "\n")
            file.write(str(monster["level"]) + "\n")
            file.write(str(monster["attack"]) + "\n")
            file.write(str(monster["health"]) + "\n")
            file.write(str(monster["max_health"]) + "\n")
            file.write(str(monster["exp"]) + "\n")


def load_game():
    global player
    global dungeon
    global florest
    global cave
    global potion
    global items
    global monsters
    with open("save.txt", "r") as file:
        player["name"] = file.readline().strip()
        player["level"] = int(file.readline().strip())
        player["attack"] = int(file.readline().strip())
        player["health"] = int(file.readline().strip())
        player["max_health"] = int(file.readline().strip())
        player["exp"] = int(file.readline().strip())
        player["max_exp"] = int(file.readline().strip())
        dungeon = file.readline().strip() == "True"
        florest = file.readline().strip() == "True"
        cave = file.readline().strip() == "True"
        potion = int(file.readline().strip())
        items.clear()
        items_count = int(file.readline().strip())
        for i in range(items_count):
            items.append(file.readline().strip())
        monsters.clear()
        while True:
            name = file.readline().strip()
            if name == "":
                break
            level = int(file.readline().strip())
            attack = int(file.readline().strip())
            health = int(file.readline().strip())
            max_health = int(file.readline().strip())
            exp = int(file.readline().strip())
            monsters.append({"name": name,
                             "level": level,
                             "attack": attack,
                             "health": health,
                             "max_health": max_health,
                             "exp": exp})


def player_level_up(player):
    if player["exp"] >= player["max_exp"]:
        player["level"] += 1
        player["exp"] = 0
        player["max_exp"] = 30 * player["level"]
        player["attack"] += 10
        player["max_health"] += 20
        player["health"] = player["max_health"]
        print("------------------------------")
        print(f"{player['name']} leveled up to {player['level']}")


def player_exp(player, monster):
    if monster["health"] <= 0:
        drop_gold()
        player["exp"] += monster["exp"]
        draw()
        print(f"{player['name']} gained {monster['exp']} experience")
        draw()


def monster_delete(monster):
    if monster["health"] <= 0:
        monsters.remove(monster)


def monster_creation(level):
    name_monster = random.choice(name_monsters)
    new_monster = {"name": name_monster,
                   "level": level,
                   "attack": 10 * level,
                   "health": 50 * level,
                   "max_health": 50 * level,
                   "exp": 13 * level,
                   }
    return new_monster


def monster_addition(monster, maps):
    for i in range(monster):
        if maps == "florest":
            random_monster = randint(1, 3)
        elif maps == "cave":
            random_monster = randint(3, 6)
        elif maps == "dungeon":
            random_monster = randint(6, 8)
        monsters.append(monster_creation(random_monster))


def show_monsters():
    os.system("clear")
    if len(monsters) == 0:
        print("No monsters")
        input("Press enter to continue")
        return
    print("MONSTERS:")
    for i in range(len(monsters)):

        draw()
        print(f"{i + 1}. {monsters[i]['name']} - Level {monsters[i]['level']} - Attack {
            monsters[i]['attack']} - Health {monsters[i]['health']} - Exp {monsters[i]['exp']}")
    draw()
    print("< back - to go back")
    draw()
    text = input("# ")
    selected_monster = monster_selection(text)
    attack(player, selected_monster)
    if text == "back":
        draw()
        print("You went back")
        draw()
        input("Press enter to continue")
        return
    show_monsters()


def monster_selection(text):
    if len(monsters) == 0:
        print("No monsters")
        return
    for i in range(len(monsters)):
        if text == f"battle {monsters[i]["name"]}" or text == f"battle {i + 1}":
            return monsters[i]
    return


def attack(player, monster):
    global potion
    os.system("clear")
    if monster is None:
        return
    while player["health"] > 0 and monster["health"] > 0:
        battle_status(player, monster)
        print("> attack")
        print("+ potion")
        print("< run")
        draw()
        choice = input("Enter your choice: ")
        if choice == "attack":
            if player["attack"] >= monster["health"]:
                monster["health"] = 0
                player["health"] -= monster["attack"]
            elif monster["attack"] >= player["health"]:
                player["health"] = 0
            else:
                monster["health"] -= player["attack"]
                player["health"] -= monster["attack"]
            battle_status(player, monster)
            time.sleep(2)
        elif choice == "potion":
            potion_use()
            potion -= 1
            time.sleep(1)
        elif choice == "run":
            print("You ran away")
            time.sleep(1)
            break
        else:
            print("Invalid input")
            time.sleep(1)
    player_exp(player, monster)
    player_level_up(player)


def battle_status(player, monster):
    os.system("clear")
    draw()
    print("\t    BATTLE")
    draw()
    print(f"> {player['name']} | Health{
          player['health']}/{player['max_health']}")
    print(f"> {monster['name']} | Health{
          monster['health']}/{monster['max_health']}")
    draw()


def player_status(player):
    os.system("clear")
    draw()
    print("\t    STATUS")
    draw()
    print(f"{player['name']}")
    print(f"Level -> {player['level']}")
    print(f"Attack -> {player['attack']}")
    print(f"Health -> {player['health']}/{player['max_health']}")
    print(f"Experience -> {player['exp']}/{player['max_exp']}")
    draw()
    input("Press enter to continue")


def menu():
    os.system("clear")
    draw()
    print("\t   MENU:")
    draw()
    print("> battle - to start a battle")
    print("& status - to show player status")
    print("# map - to select map")
    print("! monsters - to show monsters")
    print("? inventory - to show inventory")
    print("* equip - to equip items")
    print("$ loja - to go to the shop")
    print("< quit - to quit the game")
    draw()


def try_again():
    print("Do you want to play again?")
    print("\tyes\tno")
    print("------------------------------")
    choice = input("\nEnter your choice: ")
    if choice == "yes":
        reset()
        main()
    elif choice == "no":
        time.sleep(1)
        exit()
    else:
        print("Invalid input")
        try_again()


def reset():
    player["level"] = 1
    player["attack"] = 30
    player["health"] = 100
    player["max_health"] = 100
    player["exp"] = 0
    player["max_exp"] = 30


def play():
    os.system("clear")
    text = "# "
    global game_loaded

    if game_loaded:
        draw()
        print(f"    Welcome back {player['name']}")
        draw()
    else:
        name = input("Enter your name: ")
        player["name"] = name
        player_status(player)
    time.sleep(1)
    while True:
        save_game()
        menu()
        text = input("# ")

        if text == "status":
            player_status(player)
        elif text == "menu":
            menu()
        elif text == "monsters":
            show_monsters()
        elif text == "inventory":
            inventory()
        elif text == "loja":
            loja()
        elif text == "map":
            maps(select_map())
        elif text == "quit" and "exit" and "q":
            exit()
        if player["health"] <= 0:
            draw()
            print("\tGame over\n")
            draw()
            time.sleep(1)
            try_again()
            break


def maps(map):
    global dungeon, florest, cave
    if map == "dungeon":
        if dungeon:
            draw()
            print("You are already in the dungeon")
            draw()
            input("Press enter to continue")
            return
        elif player["level"] < 5:
            draw()
            print("You need to level up to 5 to enter the dungeon")
            draw()
            input("Press enter to continue")
            return
        else:
            dungeon = True
            florest = False
            cave = False
            monsters.clear()
            monster_addition(5, map)
    elif map == "florest":
        if florest:
            draw()
            print("You are already in the florest")
            draw()
            input("Press enter to continue")
            return
        else:
            florest = True
            dungeon = False
            cave = False
            monsters.clear()
            monster_addition(3, map)
    elif map == "cave":
        if cave:
            draw()
            print("You are already in the cave")
            draw()
            input("Press enter to continue")
            return
        elif player["level"] < 3:
            draw()
            print("You need to level up to 3 to enter the cave")
            draw()
        else:
            cave = True
            dungeon = False
            florest = False
            monsters.clear()
            monster_addition(2, map)
            input("Press enter to continue")
            return

    elif map == "back":
        pass


def select_map():
    os.system("clear")
    draw()
    print("\t   MAPS")
    draw()
    print("> florest - level 1")
    print("> cave - level 3")
    print("> dungeon - level 5")
    print("< back - to go back")
    draw()
    map = input("> ")
    if map == "florest" or map == "cave" or map == "dungeon" or map == "back":
        if map == "florest":
            draw()
            print("You selected the florest")
            draw()
        elif map == "cave":
            draw()
            print("You selected the cave")
            draw()
        elif map == "dungeon":
            draw()
            print("You selected the dungeon")
            draw()
        elif map == "back":
            draw()
            print("You went back")
            draw()

        input("Press enter to continue")
        return map
    else:

        select_map()


def draw():
    print("xX=------------------------=Xx")


def main_menu():
    global game_loaded
    print("Welcome to the game")
    print("1. New game")
    print("2. Load game")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        game_loaded = False
        if os.path.exists("save.txt"):
            print("There is a save file, do you want to overwrite it?")
            print("yes\tno")
            choice = input("Enter your choice: ")
            if choice == "yes":
                play()
            elif choice == "no":
                main_menu()
            else:
                print("Invalid input")
                main_menu()
        play()
    elif choice == "2":
        if os.path.exists("save.txt"):
            load_game()
            game_loaded = True
            play()
        else:
            print("No save file")
            main_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid input")
        main_menu()


def main():
    main_menu()
    save_game()


main()
