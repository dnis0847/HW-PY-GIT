from my_moduls.check_types import my_function
from my_moduls.func_colorama import print_message

def main():
    try:
        task = int(input("Выберите задание от 1 до 2: "))
        
        if task < 1 or task > 2:
            raise ValueError("Введен неправильный номер задания. Введите число от 1 до 2.")
        elif task == 1:
            my_function(1, 2)
            my_function(1, "Hello")
        elif task == 2:
            print_message("Hello, World!")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

