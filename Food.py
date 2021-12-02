from Item import *
from Ui_manager import *

class Food(Item):

    def __init__(self, name, satiety):
        super().__init__(name)
        self.satiety = satiety

    def do_it(self, stats_manager):

        Ui_manager.output(f"Вы съели {self.name}")
        stats_manager.change_hp(self.satiety)
