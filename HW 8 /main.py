import random


def main():
    task_one()


# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.

def task_one():
    list_one = []
    list_two = []
    list_count = 7
    i = 0
    while i < list_count:
        number_one = (random.uniform(0, 20))
        number_two = (random.uniform(0, 20))
        number_one = int(number_one)
        number_two = int(number_two)
        list_one.append(number_one)
        list_two.append(number_two)
        i += 1
    print(f'Первый список: {list_one}')
    print(f'Второй список: {list_two}')

    list_three = list_one + list_two
    print(f'Список который содержит в себе оба списка: {list_three}')

    set_three = set(list_three)
    list_three = list(set_three)
    print(f'Список который не повторяется: {list_three}')

    set_three = set(list_two).intersection(list_one)
    list_three = list(set_three)
    print(f'Список, который содержит общие элементы списков {list_three}')

    list_three = list_one + list_two
    unique_list = []
    for item in list_three:
        if item not in unique_list:
            unique_list.append(item)
    print(f'Список, в котором все элементы списка уникальны {unique_list}')

    list_three.clear()
    list_three.append(min(list_one))
    list_three.append(max(list_one))
    list_three.append(min(list_two))
    list_three.append(max(list_two))
    print(f'Список содержит минимальные и максимальные значения каждого из списков: {list_three}')


if __name__ == '__main__':
    main()
