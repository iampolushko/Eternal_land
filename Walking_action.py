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
            character.player.change_hp(-10)
            Ui_manager.output("Вы споткнулись, ваше HP уменьшелось на 10")
            return

        discription_index = random.randint(0, len(self.__discriptions) - 1)
        Ui_manager.output(self.__discriptions[discription_index])
