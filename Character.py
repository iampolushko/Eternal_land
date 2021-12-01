from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, stats_manager, inventory):
        self.stats_manager = stats_manager
        self.inventory = inventory

    @abstractmethod
    def use_character_ability(self):
        pass
