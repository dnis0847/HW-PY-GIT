from moduls.car import Car
from moduls.book import Book
from moduls.stadium import Stadium


def main():
    try:
        task_number = int(input("Введите номер задания: "))
        if task_number < 1 or task_number > 3:
            raise ValueError("Задание должно быть от 1 до 3")
        elif task_number == 1:
            my_car = Car()
            my_car.__str__()
            my_other_car = Car('BMW X5', '2021', 'BMW', '3.0',
                               'Красный', '5000000')
            my_other_car.__str__()
        elif task_number == 2:
            my_book = Book('Война и мир', '1867', 'АСТ',
                           'пьеса', 'Л.Н.Толстой', '1000')
            my_book.__str__()
            my_other_book = Book()
            my_other_book.__str__()
        elif task_number == 3:
            my_stadium = Stadium('Спартак', '2000', 'Россия', 'Москва', '10000')
            my_stadium.__str__()
            my_other_stadium = Stadium()
            my_other_stadium.__str__()
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
