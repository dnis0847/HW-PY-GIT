import re


# Enter task function
def enter_task():
    try:
        enter_number = input('Введите номер задания от 1-го до 3-го: ')
        enter_number = int(enter_number)
        if enter_number > 3 or enter_number < 1:
            raise ValueError('Число вне допустимого диапазона.')
        elif enter_number == 1:
            define_palindrome()
        elif enter_number == 2:
            find_reserved_words()
        elif enter_number == 3:
            сount_number_offers()
    except ValueError as err:
        print(f'Ошибка: {err}')


def define_palindrome():
    try:
        enter_str = input('Введите пожалуйста слово или фразу: ')
        enter_str = enter_str.replace(' ', '').lower()

        if enter_str == enter_str[::-1]:
            print('Введенная вами фраза является полиндромом!')
        else:
            print('Введенная вами фраза НЕ является полиндромом!')

    except ValueError as err:
        print(f'Ошибка: {err}')


def find_reserved_words():
    try:
        enter_str = input('Введите текст: ')
        enter_words = input('Введите зарезервированные слова через запятую с пробелами: ').split(sep=', ')
        for item in enter_words:
            enter_str = enter_str.replace(item, item.upper())
        print(enter_str)
    except ValueError as err:
        print(f'Ошибка: {err}')


def сount_number_offers():
    try:
        some_text = input('Введите текст: ')
        sentences = re.findall(r"[.!?](?:\s|$)", some_text)
        length = len(sentences)
        print("Количество предложений в тексте:", length)
    except ValueError as err:
        print(f'Ошибка: {err}')


if __name__ == '__main__':
    enter_task()


