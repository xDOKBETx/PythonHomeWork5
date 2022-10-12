#  Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте, как наделить бота ""интеллектом""

from random import randint


def how_many_candys_taken(name):
    taken_candy = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while taken_candy < 1 or taken_candy > 28:
        taken_candy = int(input(f"{name}, введите корректное количество конфет: "))
    return taken_candy


def value_output(name, amount, sum_of_candys, balance):
    print(f"Ходил {name}, он взял {amount}, теперь у него {sum_of_candys}. Осталось на столе {balance} конфет.")


player_human = input("Введите своё имя: ")
player_bot = "Bot"
limited_candy = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player_human}")
else:
    print(f"Первый ходит {player_bot}")

sum_of_candys_player = 0
sum_of_candys_bot = 0

while limited_candy > 28:
    if flag:
        candy = how_many_candys_taken(player_human)
        sum_of_candys_player += candy
        limited_candy -= candy
        flag = False
        value_output(player_human, candy, sum_of_candys_player, limited_candy)
    else:
        candy = randint(1, 29)
        sum_of_candys_bot += candy
        limited_candy -= candy
        flag = True
        value_output(player_bot, candy, sum_of_candys_bot, limited_candy)

if flag:
    print(f"Выиграл {player_human}")
else:
    print(f"Выиграл {player_bot}")
