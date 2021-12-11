from Item import *
from Ui_manager import *


class Money_bag(Item):

    def __init__(self, name, money_count):
        super().__init__(name)
        self.__money_count = money_count

    def do_it(self, stats_manager):
        stats_manager.change_coins_count(self.__money_count)
        Ui_manager.create_label(f"Вы получли {self.__money_count} монет")
        Ui_manager.wait_continue()
        Ui_manager.clear()
