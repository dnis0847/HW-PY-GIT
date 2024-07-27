import random

'''
Написать программу, принимающую на вход строку из 5 случайных элементов.
Программа должна передать элементы строки в односвязный список, после чего
развернуть список (аналогично list.reverse()).
'''

def generate_random_string(length):
    # Генерируем случайную строку из букв и цифр
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_string = ''.join(random.choice(chars) for _ in range(length))
    return random_string

def reverse_list(lst):
    # Развертываем список
    return lst[::-1]

def main():
    # Генерируем случайную строку
    random_string = generate_random_string(5)
    print("Случайная строка:", random_string)

    # Преобразуем строку в односвязный список
    linked_list = [char for char in random_string]
    print("Односвязный список:", linked_list)

    # Развертываем список
    reversed_list = reverse_list(linked_list)
    print("Развернутый список:", reversed_list)

if __name__ == "__main__":
    main()
