from colorama import Fore, Style
import functools

def change_color(color=Fore.WHITE):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(color + str(result) + Style.RESET_ALL)
            return result
        return wrapper
    return decorator

@change_color(Fore.YELLOW)
def print_message(message):
    return message

