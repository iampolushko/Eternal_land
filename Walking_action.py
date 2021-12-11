import random

from Game_action import *
from Character import *
from Ui_manager import *


class Walking_action(Game_action):

    def __init__(self):
        self.__discriptions = list()

    def add_discriptions(self, discriptions):
        self.__discriptions.extend(discriptions)

    def happen(self, character):
        chance = random.randint(1, 10)
        if chance == 1:
            character.stats_manager.change_hp(-10)
            Ui_manager.create_label("Вы споткнулись, ваше HP уменьшелось на 10")
            Ui_manager.wait_continue()
            Ui_manager.clear()
            return

        discription_index = random.randint(0, len(self.__discriptions) - 1)
        Ui_manager.create_label(self.__discriptions[discription_index])
        Ui_manager.wait_continue()
        Ui_manager.clear()
