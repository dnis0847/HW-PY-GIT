""" Задание 5
 Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например 5 - верхняя граница, 25 - нижняя),
их нужно поменять местами.
 """


def product_numbers_range(first_value, second_value):
    prod = 1
    if first_value > second_value:
        first_value, second_value = second_value, first_value
    for item in range(first_value, second_value):
        prod *= item
    print(prod)
