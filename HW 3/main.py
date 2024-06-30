def enter_task():
    try:
        task_number = int(input('Введите номер задания от 1-го до 4-х: '))
        if task_number < 1 or task_number > 4:
            raise ValueError('Вы ввели неправильное значение')
    except ValueError:
        print('Вы ввели не число')
        return

    if task_number == 1:
        func_task_one()
    elif task_number == 2:
        func_task_two()
    elif task_number == 3:
        func_task_three()
    elif task_number == 4:
        func_task_four()


# Task 1:
# Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на экран название дня недели.
# Например, если 1, то на экране надпись понедельник, 2 - вторник и т.д.

def func_task_one():
    try:
        enter_number = input('Введите номер дня недели: ')
        enter_number = int(enter_number)
        if enter_number < 1 or enter_number > 7:
            raise ValueError(f'Вы ввели {enter_number} такого дня недели нет, введите цифру от 1 до 7')
        else:
            if enter_number == 1:
                print(f'Вы ввели цифру {enter_number}, похоже что это Понедельник!')
            elif enter_number == 2:
                print(f'Вы ввели цифру {enter_number}, похоже что это Вторник!')
            elif enter_number == 3:
                print(f'Вы ввели цифру {enter_number}, похоже что это Среда!')
            elif enter_number == 4:
                print(f'Вы ввели цифру {enter_number}, похоже что это Четверг!')
            elif enter_number == 5:
                print(f'Вы ввели цифру {enter_number}, наконец-то Пятница!')
            elif enter_number == 6:
                print(f'Вы ввели цифру {enter_number}, Суббота выходной!')
            elif enter_number == 7:
                print(f'Вы ввели цифру {enter_number}, Воскресенье выходной!')
    except ValueError:
        print(f'Вы ввели {enter_number}, а нужно число от 1 до 7')


# Task 2
# Пользователь вводит с клавиатуры номер месяца (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

def func_task_two():
    try:
        enter_number = input('Введите номер месяца: ')
        enter_number = int(enter_number)
        if enter_number < 1 or enter_number > 12:
            raise ValueError(f'Вы ввели {enter_number} такого месяца нет, введите цифру от 1 до 12')
        else:
            if enter_number == 1:
                print(f'Вы ввели цифру {enter_number}, месяц Январь!')
            elif enter_number == 2:
                print(f'Вы ввели цифру {enter_number}, месяц Февраль!')
            elif enter_number == 3:
                print(f'Вы ввели цифру {enter_number}, месяц Март!')
            elif enter_number == 4:
                print(f'Вы ввели цифру {enter_number}, месяц Апрель!')
            elif enter_number == 5:
                print(f'Вы ввели цифру {enter_number}, месяц Май!')
            elif enter_number == 6:
                print(f'Вы ввели цифру {enter_number}, месяц Июнь!')
            elif enter_number == 7:
                print(f'Вы ввели цифру {enter_number}, месяц Июль!')
            elif enter_number == 8:
                print(f'Вы ввели цифру {enter_number}, месяц Август!')
            elif enter_number == 9:
                print(f'Вы ввели цифру {enter_number}, месяц Сентябрь!')
            elif enter_number == 10:
                print(f'Вы ввели цифру {enter_number}, месяц Октябрь!')
            elif enter_number == 11:
                print(f'Вы ввели цифру {enter_number}, месяц Ноябрь!')
            elif enter_number == 12:
                print(f'Вы ввели цифру {enter_number}, месяц Декабрь!')
    except ValueError:
        print(f'Вы ввели {enter_number}, а нужно число от 1 до 12')


# Task 3
# Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести надпись
# «Number is positive», если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»
def func_task_three():
    enter_number = input('Введите любое число: ')
    try:
        enter_number = float(enter_number)
        if enter_number > 0:
            print('Number is positive')
        elif enter_number < 0:
            print('Number is negative')
        elif enter_number == 0:
            print('Number is equal to zero')
    except ValueError:
        print('Вы ввели не число')


# Task 4
# Пользователь вводит два числа. Определить, равны ли эти числа,
# и, если нет, вывести их на экран в порядке возрастания.

def func_task_four():
    one_number = input('Введите первое число: ')
    two_number = input('Введите второе число: ')
    try:
        one_number = float(one_number)
        two_number = float(two_number)
    except ValueError:
        print('Одно или оба введеных вами значения не правильны необходимо ввести цифры')
        func_task_four()
    if one_number != two_number:
        if one_number > two_number:
            result_one = one_number
            result_two = two_number
        else:
            result_one = two_number
            result_two = one_number
        print(result_two, result_one)
    else:
        print('Введенные вами числа равны')


if __name__ == '__main__':
    enter_task()
