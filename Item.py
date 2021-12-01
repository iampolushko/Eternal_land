from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, name):
        self.name = name
        self.count = 1

    @abstractmethod  # Метод не имеющий своей реализации, при наследовании обязанны реализовать его с той же сигнатурой
    def do_it(self, stats_manager):
        pass

