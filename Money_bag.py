from Item import Item


class Money_bag(Item):

    def __init__(self, name, money_count):
        super().__init__(name)
        self.__money_count = money_count

    def do_it(self, stats_manager):
        stats_manager.change_coins_count(self.__money_count)
        print(f"Вы получли {self.__money_count} монет")
