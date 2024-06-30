""" Агрегация данных:
   Напишите функцию aggregate_data(data), которая принимает отфильтрованные данные и агрегирует их, например, 
   вычисляя суммарный объем продаж по всем периодам времени.
 """

import datetime


def aggregate_data(data):
    sales_by_month = {}
    for date, sales_list in data:
        month = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')
        if month in sales_by_month:
            sales_by_month[month] += sum(sales_list)
        else:
            sales_by_month[month] = sum(sales_list)
    return sales_by_month
