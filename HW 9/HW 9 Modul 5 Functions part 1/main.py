""" Домашнее задание Модуль 5. Функции. Тема: Функции. Часть 1. """

from sys import path
import os

path.append(os.path.join(os.path.dirname(__file__), 'my_modules'))

import task_one
import task_two
import task_three
import task_four
import task_five
import task_six
import task_seven


def main():
    try:
        task_number = input('Введите номер задания: ')
        task_number = int(task_number)
        if task_number > 7 or task_number < 1:
            raise ValueError('Введенное вами число несоответсвует номеру задания, введите цифру от 1 до 7')
        elif task_number == 1:
            task_one.display_text()
        elif task_number == 2:
            task_two.show_even_numbers(1, 22)
        elif task_number == 3:
            task_three.display_square("*", 5, True)
        elif task_number == 4:
            task_four.minimum_number(1, 5, 6, 7, 10)
        elif task_number == 5:
            task_five.product_numbers_range(5, 2)
        elif task_number == 6:
            task_six.number_of_digits(22354)
        elif task_number == 7:
            task_seven.find_palindrome(12122111)

    except ValueError as err:
        print(f'Ошибка: {err}')


if __name__ == '__main__':
    main()
