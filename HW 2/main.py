# Задание 1

# Пользователь вводит с клавиатуры три числа.
# Необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.

def amounts_production():
    first_number = input("Введите первое число ")
    second_number = input("Введите второе число ")
    first_number = int(first_number)
    second_number = int(second_number)
    print("Сумма чисел:", first_number + second_number)
    print("Произведение чисел:", first_number * second_number)


# Задание 2

# Пользователь вводит с клавиатуры три числа.
# Первое число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке,
# третье число — задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат.

def calculating_remaining_salary():
    additional_payment = input("Введите вашу зарплату: ")
    amount_payment_loan = input("Введите сумму месячного платежа по кредиту в банке: ")
    debt_communal_utilities = input("Введите сумму вашей задолженности за комунальные услуги: ")
    additional_payment = int(additional_payment)
    amount_payment_loan = int(amount_payment_loan)
    debt_communal_utilities = int(debt_communal_utilities)
    remainder_salary = additional_payment - (amount_payment_loan + debt_communal_utilities)
    print("После всех выплат у вас останется:", remainder_salary, '\u20BD')


# Задание 3

# Напишите программу, вычисляющую площадь ромба.
# Пользователь с клавиатуры вводит длину двух его диагоналей.

# (S=1/2d*b), где d и b - диагонали ромба

def area_of_the_diamond():
    first_diagonal = input("Введите первую диагональ ромба: ")
    second_diagonal = input("Введите вторую диагональ ромба: ")
    first_diagonal = int(first_diagonal)
    second_diagonal = int(second_diagonal)
    area_diamond = 0.5 * (first_diagonal * second_diagonal)
    print("Площадь ромба с диагоналями, что вы указали:", area_diamond)

# Задание 4

# Выведите на экран надпись To be or not to be на разных строках.
# Пример вывода:
# To be
# or not
# to be

def displaying_on_screen():
    print("To be", "or not", "to be", sep="\n\r")

# Задание 5

# Выведите на экран надпись
# «Life is what happens when you're busy making other plans» John Lennon
# на разных строках. Пример вывода:
#  “Life is what happens
#       when
#           you’re busy making other plans”
#                               John Lennon

def say_the_phrase():
    print('"Life is what happens', 'when', '\tyou’re busy making other plans"', sep="\n\t", end="\n\t\t\t\t\t\t\tJohn Lennon")

if __name__ == '__main__':
    # amounts_production()
    # calculating_remaining_salary()
    # area_of_the_diamond()
    # displaying_on_screen()
    say_the_phrase()