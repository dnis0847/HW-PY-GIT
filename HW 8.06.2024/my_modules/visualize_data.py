''' Визуализация результатов:
    Напишите функцию visualize_data(aggregated_data), 
    которая принимает агрегированные данные и визуализирует их, например, строит график или диаграмму.
'''

import matplotlib.pyplot as plt


def visualize_data(*aggregated_data):
    dates = []
    values = []

    for data in aggregated_data:
        dates.extend(data.keys())
        values.extend(data.values())

    plt.bar(dates, values)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Aggregated Data Visualization')
    plt.show()
