from Ui_manager import *


class Stats_manager:

    def __init__(self, hp, coins_count, damage, agility):
        self.__hp = hp
        self.__coins_count = coins_count
        self.damage = damage
        self.agility = agility
        self.__is_alive = True

    def change_hp(self, value):
        self.__hp += value

        if value > 0:
            Ui_manager.create_label(f"Вы исцелились на {value}")
            Ui_manager.wait_continue()
            Ui_manager.clear()
        if value < 0:
            Ui_manager.create_label(f"Вы получили урон {value}")
            Ui_manager.wait_continue()
            Ui_manager.clear()

        if self.__hp < 0:
            self.__is_alive = False

    def is_alive(self):
        return self.__is_alive

    def change_coins_count(self, amount):
        self.__coins_count += amount
        if self.__coins_count < 0:
            Ui_manager.create_label("У вас слишком мало деняк")
            Ui_manager.wait_continue()
            Ui_manager.clear()

    def show_stats(self):
        Ui_manager.create_label(f"У вас  {self.__hp}, HP , {self.__coins_count} Монет и {self.damage} Нанесённого урона")
        Ui_manager.wait_continue()
        Ui_manager.clear()
