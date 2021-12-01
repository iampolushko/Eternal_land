from Game_action import Game_action
from Character import Character
import random


class Walking_action(Game_action):

    def __init__(self):
        self.__discriptions = list()

    def add_discriptions(self, discriptions):
        self.__discriptions.extend(discriptions)

    def happen(self, character):
        chance = random.randint(1, 10)
        if chance == 1:
            character.player.change_hp(-10)
            print("Вы споткнулись, ваше HP уменьшелось на 10")
            return

        discription_index = random.randint(0, len(self.__discriptions) - 1)
        print(self.__discriptions[discription_index])
