from random import *

from Enemy import *
from Character import *


class Theif(Enemy):

    def __init__(self, name, damage, hp, phrase, loot, character):
        super(Theif, self).__init__(name, damage, hp, phrase, loot, character)

        self.__is_alive = True

    def change_hp(self, value):
        outcome_value = randint(1, 2)
        if outcome_value == 1:
            self.hp += value
            Ui_manager.create_label(f"Вы нанесли {value} урона")
            Ui_manager.wait_continue()
            if self.hp < 0:
                self.__is_alive = False

        if outcome_value == 2:
            player_money = self.character.stats_manager.show_coins()
            snatch_money = randint(0, player_money)
            self.character.stats_manager.change_coins_count(snatch_money)
            Ui_manager.create_label(f"Этот пидар спиздил {snatch_money} монет")
            Ui_manager.wait_continue()
            Ui_manager.clear()

    def is_alive(self):
        return self.__is_alive
