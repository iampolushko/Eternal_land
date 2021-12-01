from abc import ABC, abstractmethod


class Game_action(ABC):

    @abstractmethod
    def happen(self, character):
        pass
