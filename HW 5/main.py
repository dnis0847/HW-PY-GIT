def select_task():
    try:
        enter_number = input('Выберите номер задания: ')
        enter_number = int(enter_number)
        if enter_number > 4 or enter_number < 1:
            raise ValueError
        elif enter_number == 1:
            task_one()
        elif enter_number == 2:
            task_two()
        elif enter_number == 3:
            task_three(100, 9999)
        elif enter_number == 4:
            task_four()
    except ValueError:
        print('Вы ввели не правильное значение, нужно ввести цифру от 1 до 4-х')


# Задание 1
def task_one():
    try:
        enter_number_one = input("Введите число: ")
        enter_number_two = input("Введите степень в которую хотите ввести: ")
        enter_number_one = int(enter_number_one)
        enter_number_two = int(enter_number_two)
        result = 1
        i = 0
        while i < enter_number_two:
            result = result * enter_number_one
            i += 1
        print(result)
        raise ValueError
    except ValueError:
        print('Вы ввели не правильные значение')


# Задание 2
def task_two():
    i = 100
    count = 0
    while i <= 999:
        i = str(i)
        if i[0] == i[1]:
            count += 1
            i = int(i)
            i += 1
        elif i[1] == i[2]:
            count += 1
            i = int(i)
            i += 1
        elif i[0] == i[2]:
            count += 1
            i = int(i)
            i += 1
        else:
            i = int(i)
            i += 1
    print(count)


# Задание 3
def task_three(start, end):
    try:
        count = 0
        for number in range(start, end + 1):
            num_str = str(number)
            if len(set(num_str)) == len(num_str):
                count += 1
        print(count)
    except:
        print('Что то пошло не по плану')

# Задание 4
def task_four():
    try:
        num = input("Введите любое целое число: ")
        num = int(num)
        num_str = str(num)
        result = ""
        for char in num_str:
            if char != '3' and char != '6':
                result += char  # Добавление подходящих символов
        print("Число без цифр 3 и 6:", result)
    except:
        print('Ввести нужно число')


if __name__ == '__main__':
    select_task()


