""" roll_dice
Roll dice for multiple players.
    Author: Jack Jiang (z5129432)
    Version: v01
    Date: 28/08/2017
"""

from random import seed
from os import system
from input_players import input_players
from roll_dice import roll_dice


def play():
    player_list = input_players()
    now_rounds = 1
    while True:
        for player in player_list:
            system('cls')
            print(f'现在处于第 {now_rounds} 回合')
            print(f'{player}掷出了:\n')
            print(roll_dice())
            print('按 Ctrl+C 结束游戏.')
            input('按 Enter 键继续...')
        now_rounds += 1
    return

if __name__ == "__main__":
    seed()
    play()
