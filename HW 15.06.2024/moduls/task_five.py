"""
Написать декоратор с именем logger, который в стандартном потоке вывода ведёт журнал вызовов декорируемой функции.

В журнал необходимо внести имя вызванной функции и перечислить переданные аргументы. Ключевые аргументы должны быть перечислены с указанием ключа — имени параметра, в который эти аргументы передаются.

Помимо переданных аргументов в журнал необходимо внести использованные значения по умолчанию.

    Значения по умолчанию доступны в специальных атрибутах объекта функции __defaults__ (позиционные) и __kwdefaults__ (ключевые)

    Количество объявленных в функции строго позиционных и позиционно-ключевых параметров доступно в атрибуте функции __code__.co_argcount

В случае возникновения исключения его имя и текст также должны быть внесены в журнал, само исключение при перехвате игнорируется.

    Перехват любого исключения (в данном случае требуется перехватывать именно любое исключение, потому что декоратор может быть применён к произвольной функции) возможен при использовании базового класса Exception:
    try:
        int('a')
    except Exception:
        pass

    Доступ к объекту исключения возможен при использовании конструкции as <переменная>:
    try:
        sorted(150)
    except TypeError as exception:
        print(exception)

    Имя объекта исключения доступно во встроенном атрибуте __name__. Текст исключения (без обратной трассировки) возвращается при получении строкового представления объекта исключения.
    В примере выше в stdout будет выведено: 'int' object is not iterable.

Декоратор может применяться к функциям с различным набором позиционных и ключевых аргументов.

Написанный декоратор необходимо протестировать вручную с помощью различных дополнительных произвольных функций.
"""

import functools
import inspect


def logger(func):
    """
    Декоратор, который ведёт журнал вызовов декорируемой функции.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Получаем информацию о сигнатуре функции
        signature = inspect.signature(func)

        # Получаем значения по умолчанию для позиционных аргументов
        defaults = list(signature.parameters.values())[:len(func.__defaults__ or ())]
        positional_defaults = [f'{param.name}={value}' for param, value in zip(signature.parameters.values(), defaults)]

        # Получаем значения по умолчанию для ключевых аргументов
        keyword_defaults = {
            param.name: param.default
            for param in signature.parameters.values()
            if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default is not param.empty
        }

        # Формируем строку с переданными аргументами
        args_str = ', '.join([f'{arg}={value}' for arg, value in zip(signature.parameters.keys(), args)])
        kwargs_str = ', '.join([f'{arg}={value}' for arg, value in kwargs.items()])

        # Выводим журнал вызова функции
        print(f'{func.__name__}({args_str}, {kwargs_str}) ->', end=' ')

        try:
            result = func(*args, **kwargs)
            print(result)
            return result
        except Exception as e:
            print(f".. {type(e).__name__}: {e}")

    return wrapper


@logger
def div_round(num1, num2, *, digits=0):
    return round(num1 / num2, digits)
