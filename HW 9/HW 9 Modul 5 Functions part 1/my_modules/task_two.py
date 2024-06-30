"""Задание 2. Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа
между ними.
"""


def show_even_numbers(number_one, number_two):
    for item in range(number_one, number_two):
        if item % 2 == 0:
            print(item)
