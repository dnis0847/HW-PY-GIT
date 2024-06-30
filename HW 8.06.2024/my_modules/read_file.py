""" 1. Чтение данных:
        Напишите функцию read_file(file_path), которая принимает путь к файлу и возвращает содержимое файла
        в виде списка строк
 """


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data
