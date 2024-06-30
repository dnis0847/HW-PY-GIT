import inspect
import warnings

def check_types(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)

        # Проверяем типы аргументов
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            if param.annotation != inspect._empty and not isinstance(value, param.annotation):
                warnings.warn(f"Argument '{name}' has incorrect type. Expected: {param.annotation.__name__}, "
                              f"Got: {type(value).__name__}")

        return func(*args, **kwargs)

    return wrapper

@check_types
def my_function(arg1: int, arg2: str):
    print(arg1, arg2)

