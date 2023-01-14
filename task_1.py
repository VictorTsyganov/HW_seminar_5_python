# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint


def input_data(name):
    x = int(input(f"{name}, возьмите конфеты, от 1 до 28: "))
    while x not in range(1, 29):
        x = int(input(f"{name}, вы взяли не верное количество конфет, возьмите от 1 до 28: "))
    return x


def game_print(name, taken_sweets, counter, value):
    print(f"Ходил {name}, он взял {taken_sweets}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока или впишите имя бота,"
                " с которым хотите играть(бот 1-ого уровня - bot, бот 2-ого уровня - bot_god): ")
value = int(input("Введите количество конфет на столе: "))


def two_players_game(player1, player2, value):
    first_player = randint(0, 2)
    if first_player:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0
    counter2 = 0

    while value > 28:
        if first_player:
            taken_sweets = input_data(player1)
            counter1 += taken_sweets
            value -= taken_sweets
            first_player = False
            game_print(player1, taken_sweets, counter1, value)
        else:
            if player2 == 'bot':
                taken_sweets = randint(1, 29)
                counter2 += taken_sweets
                value -= taken_sweets
                first_player = True
                game_print(player2, taken_sweets, counter2, value)
            elif player2 == 'bot_god':
                if value % 29 == 0:
                    taken_sweets = randint(1, 29)
                else:
                    taken_sweets = value - (value // 29) * 29
                counter2 += taken_sweets
                value -= taken_sweets
                first_player = True
                game_print(player2, taken_sweets, counter2, value)
            else:
                taken_sweets = input_data(player2)
                counter2 += taken_sweets
                value -= taken_sweets
                first_player = True
                game_print(player2, taken_sweets, counter2, value)

    if first_player:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")

two_players_game(player1, player2, value)