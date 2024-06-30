""" Задание 4. Напишите функцию, удаляющую из списка целых некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов. """

def remove_number_from_list(send_number):
    my_list = [1, 3, 4, 56, 13, 2, 3, 6, 3, 17, 9, 87]
    count_number = my_list.count(send_number)
    if count_number > 0:
        for item in my_list:
            if item == send_number:
                my_list.remove(item)
    return print(count_number)
