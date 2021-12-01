from Item import Item


class Food(Item):

    def __init__(self, name, satiety):
        super().__init__(name)
        self.satiety = satiety

    def do_it(self, stats_manager):
        print(f"Вы съели {self.name}")
        stats_manager.change_hp(self.satiety)

