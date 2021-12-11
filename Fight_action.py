import random

from Game_action import *
from Ui_manager import *


class Fight_action(Game_action):

    def __init__(self, enemies):
        self.enemies = list(enemies)

    def happen(self, character):
        enemy_count = random.randint(1, int(len(self.enemies) / 10 + 1))
        Ui_manager.create_label(f"Вы наткнулись на {enemy_count} врагов")
        Ui_manager.wait_continue()
        Ui_manager.clear()
        enemies_in_fight = list()
        while True:
            enemies_in_fight.append(self.enemies[random.randint(0, len(self.enemies) - 1)])
            enemy_count -= 1
            if enemy_count == 0:
                break

        for enemy in enemies_in_fight:
            Ui_manager.create_label(f"Вы столкнудись с {enemy.name}")
            Ui_manager.wait_continue()
            Ui_manager.clear()
            Ui_manager.create_label(f"{enemy.name}: {enemy.phrase}")
            Ui_manager.wait_continue()
            Ui_manager.clear()

            while True:

                Ui_manager.create_label("Ваши действия")
                Ui_manager.add_radiobutton(input_massage="Нанести удар", value=1)
                Ui_manager.add_radiobutton(input_massage="Воспользоваться классовой способностью", value=2)
                Ui_manager.add_radiobutton(input_massage="БЕГИТ", value=3)
                result = Ui_manager.wait_result()
                Ui_manager.clear()

                player_damage = character.stats_manager.damage
                enemy_damage = enemy.damage

                if result == 1:
                    enemy.change_hp(-player_damage)
                    Ui_manager.create_label(f"Вы нанесли {player_damage} урона")
                    Ui_manager.wait_continue()
                    Ui_manager.clear()
                    character.stats_manager.change_hp(-enemy_damage)
                elif result == 2:
                    Ui_manager.create_label("Вы восползьзовались классовой способностью")
                    Ui_manager.wait_continue()
                    Ui_manager.clear()
                    character.use_character_ability()
                elif result == 3:
                    rand_int = random.randint(0, 100)
                    if rand_int < character.stats_manager.agility:
                        return
                    else:
                        character.stats_manager.change_hp(-(enemy_damage * 1.5))

                if enemy.is_alive() == False:
                    Ui_manager.create_label(f"Вы победили {enemy.name}")
                    Ui_manager.wait_continue()
                    Ui_manager.clear()
                    character.inventory.add_items(enemy.loot)
                    break

                if character.stats_manager.is_alive() == False:
                    return
