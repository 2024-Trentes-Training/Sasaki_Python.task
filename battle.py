#!/usr/bin/python3.6

import time
import random

class Battle():

    def __init__(self):
        self.player_hp = 100
        self.player_mp = 15
        self.enemy_hp = 100
        self.enemy_attack = ["1","2","3"]
        self.enemy_destiny = ["1","2","3","4","5"]

    def start(self):
        print("* 敵が現れた!\n")

        time.sleep(1)
        print(f"===============\
              \nスライム\
              \nHP {self.enemy_hp}\
              \n===============\n")
        return game.player()

    def player(self):
        time.sleep(1)
        move = input(f"* 何をする?\
                    \n\n1:攻撃 (20d)\
                    \n2:魔法攻撃 (40d MP-5)\
                    \n3:命がけ (99d HP-50 MP-9)\
                    \nHP {self.player_hp} MP {self.player_mp}\n")
        if move == "1":
            time.sleep(1)
            print("* プレイヤーの攻撃！\n")

            time.sleep(1)
            print("* 敵に20のダメージを与えた！\n")
            self.enemy_hp = self.enemy_hp - 20
        elif move == "2":
            if self.player_mp <= 4:
                time.sleep(1)
                print("MPが足りません\n")
                return game.player()
            else:
                time.sleep(1)
                print("* プレイヤーの魔法攻撃！\n")

                time.sleep(1)
                print("* 敵に40のダメージを与えた！\n")
                self.enemy_hp = self.enemy_hp - 40
                self.player_mp = self.player_mp - 5
        elif move == "3":
            if self.player_mp <= 8:
                time.sleep(1)
                print("MPが足りません\n")
                return game.player()
            else:
                time.sleep(1)
                print("*プレイヤーの命がけ！！！！")
                self.enemy_hp = self.enemy_hp - 99
                self.player_hp = self.player_hp - 50
                self.player_mp = self.player_mp - 9
                if self.player_hp <= 0 and self.enemy_hp <= 0:
                    time.sleep(1)
                    print("両者のHPが0になりました")

                    time.sleep(1)
                    print("[Drow]")
        else:
            time.sleep(1)
            print("もう一度入力してください\n")
            return game.player()

        time.sleep(1)
        print(f">>>敵のHP {self.enemy_hp}\n")
        if self.enemy_hp <= 0:
            return game.status()
        elif self.enemy_hp == 1:
            key = random.choice(self.enemy_destiny)
            if key == "1":
                time.sleep(1)
                print("敵のスライムが覚醒状態になりました\n")
                self.enemy_hp = 500
                time.sleep(1)
                print(f"==========\
                     \n覚醒スライム\
                     \nHP {self.enemy_hp}\
                     \n==========\n")
                return game.awakening()
        
        return game.enemy()

    def awakening(self):
        time.sleep(1)
        print("* 敵のターン！\n")

        time.sleep(1)
        print("* プレイヤーに300のダメージを与えた！\n")
        self.player_hp = self.player_hp - 300

        time.sleep(1)
        print(f">>>プレイヤーのHP {self.player_hp}\n")
        return game.status()

    def enemy(self):

        time.sleep(1)
        print("* 敵のターン！\n")

        if self.enemy_hp == 1:
            self.enemy_destiny = ["1"]
            move = 3
        else:
            move = random.choice(self.enemy_attack)

        if move == "1":
            time.sleep(1)
            print("* プレイヤーに10のダメージを与えた！\n")
            self.player_hp = self.player_hp - 10

            time.sleep(1)
            print(f">>>プレイヤーのHP {self.player_hp}\n")

        elif move == "2":
            time.sleep(1)
            print("* プレイヤーに30のダメージを与えた！\n")
            self.player_hp = self.player_hp - 30

            time.sleep(1)
            print(f">>>プレイヤーのHP {self.player_hp}\n")
        else:
            time.sleep(1)
            print("* 敵はHPを20回復した\n")
            if self.enemy_hp == 100:
                time.sleep(1)
                print("しかしHPは満タンだ\n")
            else:
                self.enemy_hp = self.enemy_hp + 20
                if self.enemy_hp >= 100:
                    self.enemy_hp = 100

                time.sleep(1)
                print(f">>>敵のHP {self.enemy_hp}\n")

        return game.status()

    def status(self):
        if self.player_hp <= 0:

            time.sleep(1)
            print("* プレイヤーのHPが0になりました\n")

            time.sleep(1)
            return "[Lose]"
        elif self.enemy_hp <= 0:
            time.sleep(1)
            print("* 敵のHPが0になりました\n")

            time.sleep(1)
            return "[Win]"
        else:
            time.sleep(1)
            print(f"現在のHPです\
                  \nプレイヤー HP {self.player_hp}\
                  \n敵 HP {self.enemy_hp}\n")
            return game.player()

game = Battle()
print(game.start())
