class Enemy():

    def __init__(self, name, damage, hp, phrase, loot):
        self.name = name
        self.damage = damage
        self.__hp = hp
        self.loot = list(loot)
        self.phrase = phrase
        self.__is_alive = True

    def change_hp(self, value):
        self.__hp += value
        if self.__hp < 0:
            self.__is_alive = False

    def is_alive(self):
        return self.__is_alive
