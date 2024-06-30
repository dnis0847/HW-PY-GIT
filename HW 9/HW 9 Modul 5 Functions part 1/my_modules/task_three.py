""" Задание 3.
Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
"""


def display_square(symbol, n, fill=True):
    line = n * symbol
    if fill:
        for _ in range(n):
            print(line)
    else:
        print(line)
        for _ in range(n - 2):
            print(symbol + " " * (n - 2) + symbol)
        print(line)