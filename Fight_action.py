from Game_action import Game_action
import random


class Fight_action(Game_action):

    def __init__(self, enemies):
        self.enemies = list(enemies)

    def happen(self, character):
        enemy_count = random.randint(1, int(len(self.enemies) / 10 + 1))
        print(f"Вы наткнулись на {enemy_count} врагов")
        enemies_in_fight = list()
        while True:
            enemies_in_fight.append(self.enemies[random.randint(0, len(self.enemies) - 1)])
            enemy_count -= 1
            if enemy_count == 0:
                break

        for enemy in enemies_in_fight:
            print(f"Вы столкнудись с {enemy.name}")
            print(f"{enemy.name}: {enemy.phrase}")
            option = None

            while True:

                while True:
                    print("Ваши действия: 1)Нанести удар 2)Воспользоваться классовой способностью 3)БЕГИТ")
                    try:
                        option = int(input())
                        break
                    except:
                        print("Неверный ввод")

                player_damage = character.stats_manager.damage
                enemy_damage = enemy.damage

                if option == 1:
                    enemy.change_hp(-player_damage)
                    print(f"Вы нанесли {player_damage} урона")
                    character.stats_manager.change_hp(-enemy_damage)
                elif option == 2:
                    print("Вы восползьзовались классовой способностью")
                    character.use_character_ability()
                elif option == 3:
                    result = random.randint(0, 100)
                    if result < character.stats_manager.agility:
                        return
                    else:
                        character.stats_manager.change_hp(-(enemy_damage * 1.5))
                else:
                    print("Неправельный ввод")

                if enemy.is_alive() == False:
                    print(f"Вы победили {enemy.name}")
                    character.inventory.add_items(enemy.loot)
                    break

                if character.stats_manager.is_alive() == False:
                    return
