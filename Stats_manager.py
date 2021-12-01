class Stats_manager:

    def __init__(self, hp, coins_count, damage, agility):
        self.__hp = hp
        self.__coins_count = coins_count
        self.damage = damage
        self.agility = agility
        self.__is_alive = True

    def change_hp(self, value):
        self.__hp += value

        if value > 0:
            print(f"Вы исцелились на {value}")
        if value < 0:
            print(f"Вы получили урон {value}")

        if self.__hp < 0:
            self.__is_alive = False

    def is_alive(self):
        return self.__is_alive

    def change_coins_count(self, amount):
        self.__coins_count += amount
        if self.__coins_count < 0:
            print("У вас слишком мало деняк")

    def show_stats(self):
        print("У вас ", self.__hp, "HP ,", self.__coins_count, "Монет и", self.damage, "Нанесённого урона")
