import random

from Stats_manager import Stats_manager
from Food import Food
from Walking_action import Walking_action
from Inventory import Inventory
from Game_manager import Game_manager
from Money_bag import Money_bag
from Character import Character
from Alchemist import Alchemist
from Enemy import Enemy
from Fight_action import Fight_action


def main():

    stats_manager = Stats_manager(hp=100, coins_count=10, damage=15, agility=10)

    inventory = Inventory()

    character = None
    print("Ты кто по масти?: 1 - Алхимик; 2 - Крашнуть проект")

    while True:
        try:
            character_choice = int(input())
            break
        except:
            print("Вы ввели неправельный ввод")

    if character_choice == 1:
        character = Alchemist(stats_manager, inventory)
    elif character_choice == 2:
        character = Character(stats_manager, inventory)

    apple = Food("apple", 5)
    inventory.add_item(apple)
    cum = Food("cum", 10)
    inventory.add_item(cum)
    kids = Food("kids", 1)
    inventory.add_item(kids)

    money_quantity = random.randint(1, 100)
    purse = Money_bag("purse", money_quantity)
    inventory.add_item(purse)

    game_manager = Game_manager(character)

    walking_action = Walking_action()
    walking_action.add_discriptions(["Лес х*ёв", "Океае дерьма", "Джунгли бывшей"])

    game_manager.add_action(walking_action)

    enemy1 = Enemy("Васян", 10, 20, "Плотная всем нашим", [cum, kids])
    enemy2 = Enemy("Ержан", 5, 10, "За работу", [apple])

    fight_action = Fight_action([enemy1, enemy2])
    game_manager.add_action(fight_action)

    print("Добро пожаловать в EternalLand")
    while True:
        print("Что вы желаете сделать? 1)Идти дальше; 2)Открыть инвентарь; 3)Посмотреть статы персонажа")

        while True:
            try:
                choise = int(input())
                break
            except:
                print("Вы ввели неверный ввод")

        if choise == 1:
            game_manager.uptade()

        elif choise == 2:
            game_manager.open_inventory()

        elif choise == 3:
            stats_manager.show_stats()

        elif choise == 666:
            break

        else:
            print("Вы ввели говно")

        if character.stats_manager.is_alive() == False:
            print("Ты и твоя мать мертвы")
            break


if __name__ == "__main__":  # Провеяет является ли Main.py зпускным файлом
    main()
