"""
Написать функцию высшего порядка с именем math_function_resolver, которая вычисляет округлённые значения для различных математических функций.

Функция принимает обязательным аргументом математическую функцию, произвольное количество значений x для математической функции и необязательным аргументом переключатель: тип вычисляемых значений float или str.

    Математическая функция должна быть строго позиционным аргументом, передаётся в виде вызываемого объекта.
        Данная функция должна принимать один обязательный позиционно-ключевой аргумент — число x, для которого необходимо вычислить значение математической функции. Это должно быть описано в документации к функции высшего порядка.

    Значения x для математической функции должны быть строго позиционными, передаются в виде произвольного кортежа объектов int или float.

    Переключатель должен быть строго ключевым, передаётся в виде объекта bool, значение по умолчанию False (тип вычисляемых значений float).

Функция возвращает объект списка с вычисленными значениями математической функции для переданных значений x. Значения должны быть математичеси округлены до целого.

    Элементами списка должны быть объекты int или объекты str в зависимости от значения аргумента переключателя.

В данной задаче необходимо минимизировать количество итераций.

Написанную функцию необходимо протестировать вручную.
Пример ручного теста:
    math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
    [2, 3, 4, 4, 4, 5, 6, 6, 6]

    math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
    [2, 1, 0, 0, 0, -1, -2, -2, -2]

    math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
    ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']
"""


def math_function_resolver(func, *args, res_to_str=False):
    result = [round(func(x)) if not res_to_str else str(round(func(x))) for x in args]
    return result

