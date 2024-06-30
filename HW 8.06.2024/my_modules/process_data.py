""" 2. Обработка данных:
   Напишите функцию process_data(data), которая принимает список строк с данными о продажах и преобразует их
   в удобный формат (например, словарь с информацией о продажах для каждого периода времени). """


def process_data(data):
    result = {}
    current_period = None
    current_sales = []

    for line in data:
        if line.strip() == '':
            if current_period is not None:
                result[current_period] = current_sales
                current_sales = []
        else:
            date, value = line.strip().split(',')
            date = date.strip()
            value = int(value.strip())

            if current_period is None or date != current_period:
                current_period = date
                current_sales = []

            current_sales.append(value)

    if current_period is not None:
        result[current_period] = current_sales

    return result
