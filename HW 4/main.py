def enter_task():
    try:
        task_number = int(input('Введите номер задания от 1-го до 4-х: '))
        if task_number < 1 or task_number > 4:
            raise ValueError('Вы ввели неправильное значение')
    except ValueError:
        print('Вы ввели неправильное значение')
        return

    if task_number == 1:
        func_task_one()
    elif task_number == 2:
        func_task_two()
    elif task_number == 3:
        func_task_three()
    elif task_number == 4:
        func_task_four()


# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без остатка)
# нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число.
# Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.

def func_task_one():
    while True:  # Начало бесконечного цикла для повторного ввода, если возникнет ошибка
        try:
            enter_number = int(input('Введите целое число в диапазоне от 1 до 100: '))
            if enter_number < 1 or enter_number > 100:
                raise ValueError('Число вне допустимого диапазона.')
            break  # Прерываем цикл, если было введено корректное значение
        except ValueError as e:  # Обработка исключения для некорректного ввода или значения вне диапазона
            print(f'Ошибка: {e}. Попробуйте снова.')

    # После получения корректного ввода, следует проверка на делимость
    if enter_number % 5 == 0 and enter_number % 3 == 0:
        print('Fizz Buzz')
    elif enter_number % 5 == 0:
        print('Buzz')
    elif enter_number % 3 == 0:
        print('Fizz')
    else:
        print(enter_number)


# Задание 2
# Написать программу, которая по выбору пользователя возводит
# введенное им число в степень от нулевой до седьмой включительно.

def func_task_two():
    try:
        enter_number = int(input('Введите число: '))
        degree = int(input('Введите степень числа от 0 до 7 включительно: '))
        if degree < 0 or degree > 7:
            raise ValueError('Введенная степень вне допустимого диапазона')
        else:
            result = enter_number ** degree
            print(result)
    except ValueError as err:
        print(f'Ошибка: {err}. Попробуйте снова.')


# Задание 3
# Написать программу подсчета стоимости разговора для разных мобильных операторов.
# Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.
def func_task_three():
    while True:
        try:
            question = input("\nВыберите оператора на который вы звоните(Укажите цифру): "
                             "\n1 - Билайн \n2 - Теле2 \n3 - Мегафон \n4 - Мтс \n\n>>> ")
            if question not in ['1', '2', '3', '4']:
                raise ValueError("Неверный номер оператора. Попробуйте еще раз.")

            a = float(input("\nВведите стоимость разговора за минуту: "))
            if a < 0:
                raise ValueError("Стоимость не может быть отрицательной. Пожалуйста, введите корректное значение.")

            b = float(input("Введите кол-во минут: "))
            if b < 0:
                raise ValueError(
                    "Количество минут не может быть отрицательным. Пожалуйста, введите корректное значение.")

            c = a * b
            print(f"За {b} минут разговора вы потратите {c} Рублей")

        except ValueError as e:
            print(f"Ошибка: {e}\nПожалуйста, введите корректные данные.")
        else:
            break

    input("\nНажмите Enter чтобы завершить программу")
    print("\nСпасибо за использование!")


def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission_rate = 0.03
    elif sales <= 1000:
        commission_rate = 0.05
    else:
        commission_rate = 0.08
    return base_salary + (sales * commission_rate)


def func_task_four():
    sales_levels = []
    for i in range(1, 4):
        while True:
            try:
                sales = float(input(f"Введите уровень продаж для менеджера {i}: "))
                if sales < 0:
                    print("Уровень продаж не может быть отрицательным. Пожалуйста, попробуйте снова.")
                else:
                    sales_levels.append(sales)
                    break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовое значение.")

    salaries = [calculate_salary(sales) for sales in sales_levels]
    best_sales_index = salaries.index(max(salaries))

    print("\nЗарплаты менеджеров:")
    for i, salary in enumerate(salaries, start=1):
        if i == best_sales_index + 1:
            salary += 200  # Премия лучшему менеджеру
            print(f"Менеджер {i}: {salary}$ (включая премию)")
        else:
            print(f"Менеджер {i}: {salary}$")

    print(f"\nЛучший менеджер: Менеджер {best_sales_index + 1}")


if __name__ == '__main__':
    enter_task()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

