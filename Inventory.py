from Stats_manager import Stats_manager
from Item import Item


class Inventory:

    def __init__(self):
        self.__items = list()

    def add_item(self, item):
        if item in self.__items:
            item.count += 1
        else:
            self.__items.append(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def remove_item(self, item):
        if item in self.__items == False:
            raise Exception("Указанного предмета не существует в инвентаре")
            return

        if item.count > 1:
            item.count -= 1
        else:
            self.__items.remove(item)

    def get_item_from_name(self, item_name):
        sought_item = None
        for item in self.__items:
            if item_name == item.name:
                sought_item = item

        if sought_item == None:
            raise Exception("Не удалось найти предмет")
            return

        return sought_item

    def use_item(self, item, stats_manager):
        if item in self.__items == False:
            raise Exception("Указанного предмета не существует в инвентаре")
            return

        item.do_it(stats_manager)
        self.remove_item(item)

    def get_items_names(self):
        names = "| "

        for item in self.__items:
            names += item.name + " X" + str(item.count) + " | "

        return names
