import random

from Game_action import *
from Ui_manager import *
import Traider_action
import Character
from Stats_manager import *


class Town_action(Game_action):

    def __init__(self, healing_drink, apple):
        self.healing_drink = healing_drink
        self.apple = apple
        self.time = 0



    def happen(self, character):
        Ui_manager.create_label("Вы набрели на город")

        Ui_manager.add_radiobutton(input_massage="Войти в город", value=1)
        Ui_manager.add_radiobutton(input_massage="Пройти мимо", value=2)

        result = Ui_manager.wait_result()
        Ui_manager.clear()


        if result == 1:
            while True:

                if self.time == 0:

                    Ui_manager.create_label("Чем вы хотите занятся?")
                    Ui_manager.add_radiobutton(input_massage="Зайти к целителю", value=1)
                    Ui_manager.add_radiobutton(input_massage="Зайти к оружейнику", value=2)
                    Ui_manager.add_radiobutton(input_massage="Зайти к трактирщику", value=3)
                    Ui_manager.add_radiobutton(input_massage="Подождать сутки", value=4)
                    Ui_manager.add_radiobutton(input_massage="Покинуть город", value=1000)
                    result = Ui_manager.wait_result()
                    Ui_manager.clear()

                    # Целитель
                    if result == 1:
                        while True:
                            Ui_manager.create_label("Целитель: Привет, тебя подлатать?")
                            Ui_manager.add_radiobutton("10 xp - 10 монет", value=1)
                            Ui_manager.add_radiobutton("50 xp - 47 монет", value=2)
                            Ui_manager.add_radiobutton("100 xp - 90 монет", value=3)
                            Ui_manager.add_radiobutton("Зелье исцеления", value=4)
                            Ui_manager.add_radiobutton("Уйти", value=1000)

                            result = Ui_manager.wait_result()
                            Ui_manager.clear()

                            if result == 1:
                                character.stats_manager.change_hp(10)
                                character.stats_manager.change_coins_count(-10)

                            elif result == 2:
                                character.stats_manager.change_hp(50)
                                character.stats_manager.change_coins_count(-47)

                            elif result == 3:
                                character.stats_manager.change_hp(100)
                                character.stats_manager.change_coins_count(-90)

                            elif result == 4:
                                character.inventory.add_item(self.healing_drink)

                            else:
                                break
                    #Оружейник
                    elif result == 2:
                        while True:
                            Ui_manager.create_label("Оружейник: Привет, хочешь приобрести новое оружие?")
                            Ui_manager.add_radiobutton("Вилка 'Зелёный слоник', наносит 10 урона, стоит 10 монет", value=1)
                            Ui_manager.add_radiobutton("Карабинный дробовик винтовочного типа, наносит 15 урона, стоит 1000", value=2)
                            Ui_manager.add_radiobutton("Меч 'Мятежник' из DMC, наносит 100 урона, стоит твоей души и 100 монет", value=3)
                            Ui_manager.add_radiobutton("Уйти", value=1000)
                            result = Ui_manager.wait_result()
                            Ui_manager.clear()
                            if result == 1:
                                character.stats_manager.change_player_damage(10)
                            elif result == 2:
                                character.stats_manager.change_player_damage(15)
                            elif result == 3:
                                character.stats_manager.change_player_damage(100)
                            else:
                                break
                    #Трактирщик
                    elif result == 3:
                        while True:
                            Ui_manager.create_label("Трактирщик: Привет, хочешь пополнить запасы припасов?")
                            Ui_manager.add_radiobutton("Яблоко - 10 монет", value=1)
                            Ui_manager.add_radiobutton("Уйти", value=1000)
                            result = Ui_manager.wait_result()
                            Ui_manager.clear()
                            if result == 1:
                                Ui_manager.create_label("Вы купили яблоко")
                                character.inventory.add_item(self.apple)
                            else:
                                break


                    elif result == 4:
                        None





                #Покинуть город
                else:
                    break







