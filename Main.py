import random
from tkinter import *

from Stats_manager import *
from Food import *
from Walking_action import *
from Inventory import *
from Game_manager import *
from Money_bag import *
from Character import *
from Alchemist import *
from Enemy import *
from Dodger import *
from Fight_action import *
from Ui_manager import *
from Theif import *
from Traider_action import *
from Town_action import Town_action


def main():

    Ui_manager.run()

    stats_manager = Stats_manager(hp=1000, coins_count=100, damage=15, agility=10)
    inventory = Inventory()

    character = None
    Ui_manager.create_label("Ты кто по масти?: 1 - Алхимик; 2 - Крашнуть проект")

    Ui_manager.add_radiobutton(input_massage="Алхимик", value=1)
    Ui_manager.add_radiobutton(input_massage="Крашнуть проект", value=2)

    result = Ui_manager.wait_result()

    if result == 1:
        character = Alchemist(stats_manager, inventory)
    elif result == 2:
        character = Character(stats_manager, inventory)

    Ui_manager.clear()

    apple = Food("apple", 5)
    inventory.add_item(apple)
    cum = Food("cum", 10)
    inventory.add_item(cum)
    kids = Food("kids", 1)
    inventory.add_item(kids)

    money_quantity = 1
    purse = Money_bag("purse", money_quantity)
    inventory.add_item(purse)

    game_manager = Game_manager(character)

    walking_action = Walking_action()
    walking_action.add_discriptions(["Лес х*ёв", "Океаен дерьма", "Джунгли бывшей"])

    game_manager.add_action(walking_action)

    enemy1 = Enemy("Васян", 10, 20, "Плотная всем нашим", [cum, kids], character)
    enemy2 = Enemy("Ержан", 5, 10, "За работу", [apple], character)
    enemy3 = Dodger("Ловкий", 3, 10, "Резкий, дерзкий", [purse], character=character)
    enemy4 = Theif(name="Робин BAD", damage=10, hp=10, phrase="У тебя есть монеты, а я могу дать пизды", loot=[purse], character=character )

    fight_action = Fight_action([enemy1,enemy2,enemy3,enemy4])
    game_manager.add_action(fight_action)

    traider_action = Traider_action([apple, cum])
    game_manager.add_action(traider_action)

    healing_drink = Food("Зелье исциления", 50)
    town_action = Town_action(healing_drink=healing_drink, apple=apple)
    game_manager.add_action(town_action)


    Ui_manager.create_label("Добро пожаловать в EternalLand")
    Ui_manager.wait_continue()
    Ui_manager.clear()

    while True:
        Ui_manager.create_label("Что вы желаете сделать?")

        Ui_manager.add_radiobutton(input_massage="Идти дальше", value=1)
        Ui_manager.add_radiobutton(input_massage="Открыть инвентарь", value=2)
        Ui_manager.add_radiobutton(input_massage="Посмотреть статы персонажа", value=3)
        result = Ui_manager.wait_result()
        Ui_manager.clear()

        if result == 1:
            game_manager.uptade()

        elif result == 2:
            game_manager.open_inventory()

        elif result == 3:
            stats_manager.show_stats()

        if character.stats_manager.is_alive() == False:
            Ui_manager.create_label("Ты и твоя мать мертвы")
            Ui_manager.wait_continue()
            Ui_manager.clear()
            break


if __name__ == "__main__":  # Провеяет является ли Main.py зпускным файлом
    main()
