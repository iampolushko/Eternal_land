from random import *

from Character import *
from Enemy import *
from Ui_manager import *


class Dodger(Enemy):

    def __init__(self, name, damage, hp, phrase, loot, character):
        super(Dodger, self).__init__(name, damage, hp, phrase, loot, character)

        self.__is_alive = True

    def change_hp(self, value):
        outcome_value = randint(1, 3)
        if outcome_value == 1:
            self.hp += value
            Ui_manager.create_label(f"Вы нанесли {value} урона")
            Ui_manager.wait_continue()
            if self.hp < 0:
                self.__is_alive = False

        if outcome_value == 2:
            Ui_manager.create_label("Противник увернулся от удра")
            Ui_manager.wait_continue()
            Ui_manager.clear()

        if outcome_value == 3:
            self.character.stats_manager.change_hp(value)
            Ui_manager.create_label(f"Противник парировал удар и нанёс вам {value} урона")
            Ui_manager.wait_continue()
            Ui_manager.clear()

    def is_alive(self):
        return self.__is_alive
