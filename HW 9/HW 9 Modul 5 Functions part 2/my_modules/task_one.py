""" Задание 1. Напишите функцию, вычесляющую произведение элементов списка целых. Список передается в качестве
параметра. Полученный результат возвращается из функции. """

from math import prod

def product_list_items(list_items):
    result = prod(list_items)
    return print(f'Произведение введенных вами элементов списка равно: {result}')