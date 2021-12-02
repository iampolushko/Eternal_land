from Character import *


class Alchemist(Character):
    def __init__(self, stats_manager, inventory):
        super().__init__(stats_manager, inventory)

    def use_character_ability(self):
        self.stats_manager.change_hp(10)
