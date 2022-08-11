import random
from random import *

from Game_action import *
from Character import *
from Ui_manager import *
from Food import *
from Inventory import *


class Traider_action(Game_action):

    def __init__(self, traider_items):
        self.traider_items = list(traider_items)

    def happen(self, character):
        Ui_manager.create_label("Вы встретили торговца")

        Ui_manager.add_radiobutton(input_massage="Зайти к трговцу", value=1)
        Ui_manager.add_radiobutton(input_massage="Пройти мимо", value=2)

        result = Ui_manager.wait_result()
        Ui_manager.clear()

        tick = 0
        price = None
        if result == 1:
            for item in self.traider_items:
                tick += 1
                price = randint(1, 10)
                Ui_manager.add_radiobutton(input_massage=f"{item.name} за {price}", value=tick)
            Ui_manager.add_radiobutton(input_massage="Ничего не покупать", value=tick + 1)
            traider_item_num = Ui_manager.wait_result()

            if traider_item_num != tick + 1:
                character.inventory.add_item(self.traider_items[traider_item_num - 1])
                character.stats_manager.change_coins_count(-price)

        Ui_manager.clear()
