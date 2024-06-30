import moduls.task_one
import moduls.task_two
import moduls.task_three
import moduls.task_four
import moduls.task_five

def main():
    try:
        enter_number = int(input('Выберите задание от 1 до 5: '))
        if enter_number < 1 or enter_number > 5:
            raise ValueError("Введен неправильный номер задания. Введите число от 1 до 5.")
        elif enter_number == 1:
            print(moduls.task_one.pick_resistors(112))
            print(moduls.task_one.pick_resistors(549))
        elif enter_number == 2:
            deck_generator = moduls.task_two.deck()
            deck_list = list(deck_generator)
            print(deck_list[::13])
        elif enter_number == 3:
            print(moduls.task_three.math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10)))
            print(moduls.task_three.math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10)))
            print(moduls.task_three.math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True))
        elif enter_number == 4:
            moduls.task_four.testing_function()
        elif enter_number == 5:
            moduls.task_five.div_round(1, 3, digits=2)
            moduls.task_five.div_round(7, 2)
            moduls.task_five.div_round(5, 0)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
