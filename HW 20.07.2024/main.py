import moduls.task_one as t1
import moduls.task_two as t2

def main():
    task_number = int(input('Введите номер задания от 1 до 2: '))
    if task_number > 2 or task_number < 1:
        try:
            raise ValueError
        except ValueError:
            print('Вы ввели неправильное значение')
            return
    elif task_number == 1:
        my_stack = t1.StringStack(2)
        my_stack.menu()
    elif task_number == 2:
        my_stack = t2.StringStack()
        my_stack.menu()

if __name__ == '__main__':
    main()
