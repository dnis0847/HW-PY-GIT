""" Фильтрация данных:
   Напишите функцию filter_data(data, threshold), которая принимает обработанные данные и пороговое значение 
   threshold для фильтрации. Функция должна вернуть только те записи о продажах, 
   у которых объем продаж превышает threshold.
"""


def filter_data(data, threshold):
    result = []
    for period, sales in data.items():
        if sum(sales) > threshold:
            result.append((period, sales))
    return result
