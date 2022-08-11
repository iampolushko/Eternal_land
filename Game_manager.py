import random
import sys
import traceback

from Inventory import Inventory
from Stats_manager import Stats_manager
from Ui_manager import *


class Game_manager:

    def __init__(self, character):
        self.__character = character
        self.__game_actions = list()

    def open_inventory(self):
        inventory = self.__character.inventory
        items_mass = []
        for item_name in inventory.get_items_name_to_list():
            items_mass.append(item_name)

        Ui_manager.create_label(f"У вас в инвенторе {items_mass} "
                                f"\nЧто делать дальше?")

        Ui_manager.add_radiobutton(input_massage="Исп предмет", value=1)
        Ui_manager.add_radiobutton(input_massage="Закрыть инвентарь", value=2)
        result = Ui_manager.wait_result()
        Ui_manager.clear()

        if result == 1:
            inventory = self.__character.inventory

            Ui_manager.create_label("Какой предмет вы хотите использовать?")
            i = 1
            for item_name in inventory.get_items_name_to_list():
                Ui_manager.add_radiobutton(input_massage=item_name, value=i)
                i += 1
            Ui_manager.add_radiobutton(input_massage="Закрыть инвентарь", value=1000)

            index = Ui_manager.wait_result()
            Ui_manager.clear()

            if index == 1000:
                return
            else:
                item = inventory.get_item_from_index(index - 1)

                inventory.use_item(item, self.__character.stats_manager)

        elif result == 2:
            return

    def add_action(self, action):
        self.__game_actions.append(action)

    def uptade(self):
        if len(self.__game_actions) < 1:
            raise Exception("Ошибка вызова uptade")

            return

        action_num = random.randint(0, len(self.__game_actions) - 1)
        rand_action = self.__game_actions[action_num]
        rand_action.happen(self.__character)
