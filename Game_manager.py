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
        Ui_manager.output(self.__character.inventory.get_items_names())

        Ui_manager.output("Что делать дальше?: 1 - Исп предмет; 2 - Закрыть инвентарь")

        while True:
            try:
                option = Ui_manager.input_int()
                break
            except:
                Ui_manager.output("Вы ввели неверный ввод")

        if option == 1:

            while True:
                try:
                    Ui_manager.output("Введите имя предмета, который хотите использовать")
                    item_name = Ui_manager.input()
                    item = self.__character.inventory.get_item_from_name(item_name)
                    break
                except Exception as exc:

                    Ui_manager.output(exc)

            if item == None:
                return

            inventory = self.__character.inventory
            inventory.use_item(item, self.__character.stats_manager)

        elif option == 2:
            return
        else:
            Ui_manager.output("Вы ввели неверное число")
            return


    def add_action(self, action):
        self.__game_actions.append(action)

    def uptade(self):
        if len(self.__game_actions) < 1:
            raise Exception("Ошибка вызова uptade")

            return #Ретёрн точно нужен?

        action_num = random.randint(0, len(self.__game_actions)-1)
        rand_action = self.__game_actions[action_num]
        rand_action.happen(self.__character)