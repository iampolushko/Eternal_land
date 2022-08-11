from Ui_manager import *
from Character import *


class Enemy():

    def __init__(self, name, damage, hp, phrase, loot, character):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.phrase = phrase
        self.loot = list(loot)
        self.character = character
        self.__is_alive = True

    def change_hp(self, value):
        self.hp += value
        Ui_manager.create_label(f"Вы нанесли {value} урона")
        Ui_manager.wait_continue()
        if self.hp < 0:
            self.__is_alive = False

    def is_alive(self):
        return self.__is_alive
