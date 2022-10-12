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


first_player = input("Первый игрок, введите своё имя: ")
second_player = input("Второй игрок, введите своё имя: ")
limited_candy = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первым ходит {first_player}")
else:
    print(f"Первым ходит {second_player}")

sum_of_candys_first_player = 0
sum_of_candys_second_player = 0

while limited_candy > 28:
    if flag:
        candy = how_many_candys_taken(first_player)
        sum_of_candys_first_player += candy
        limited_candy -= candy
        flag = False
        value_output(first_player, candy, sum_of_candys_first_player, limited_candy)
    else:
        candy = how_many_candys_taken(second_player)
        sum_of_candys_second_player += candy
        limited_candy -= candy
        flag = True
        value_output(second_player, candy, sum_of_candys_second_player, limited_candy)

if flag:
    print(f"Выиграл {first_player}")
else:
    print(f"Выиграл {second_player}")
