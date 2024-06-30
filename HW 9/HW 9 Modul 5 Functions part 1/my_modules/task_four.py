""" Задание 4:
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров.
"""

def minimum_number(number_one, number_two, number_three, number_four, number_five):
    min_number = min(number_one, number_two, number_three, number_four, number_five)
    print(min_number)
