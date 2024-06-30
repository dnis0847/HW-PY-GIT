""" Домашнее задание Модуль 5. Функции. Тема: Функции. Часть 2. """

from sys import path
import os

path.append(os.path.join(os.path.dirname(__file__), 'my_modules'))

import task_one
import task_two
import task_three
import task_four
import task_five
import task_six

def main():
    try:
        task_number = input('Введите номер задания: ')
        task_number = int(task_number)
        if task_number > 6 or task_number < 1:
            raise ValueError('Введенное вами число несоответсвует номеру задания, введите цифру от 1 до 6')
        elif task_number == 1:
            task_one.product_list_items([1, 2, 3, 4, 5])
        elif task_number == 2:
            task_two.min_list_items([1, 2, 0, 4, 5])
        elif task_number == 3:
            task_three.search_prime_numbers([1, 2, 6, 4, 5])
        elif task_number == 4:
            task_four.remove_number_from_list(13)
        elif task_number == 5:
            task_five.get_general_list([1, 2, 3], [4, 5, 6])
        elif task_number == 6:
            task_six.get_list_degree([1, 2, 3, 4, 5], 3)

    except ValueError as err:
        print(f'Ошибка: {err}')


if __name__ == '__main__':
    main()
