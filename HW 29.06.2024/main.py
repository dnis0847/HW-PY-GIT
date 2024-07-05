from moduls.car import Car
from moduls.book import Book
from moduls.stadium import Stadium

def main():
    try:
        task_number = int(input("Введите номер задания: "))
        if task_number < 1 or task_number > 3:
            raise ValueError("Задание должно быть от 1 до 3")
        elif task_number == 1:
            my_car = Car('Audi A6', '2020', 'Audi', '2.0',
                         'Черный', '1000000')
            my_car.get_data()
            my_car.set_name()
            my_car.get_data()
            other_car = Car('BMW X5', '2021', 'BMW', '3.0',
                             'Красный', '5000000')
            other_car.get_data()
        elif task_number == 2:
            my_book = Book('Война и мир', '1867', 'АСТ',
                           'пьеса', 'Л.Н.Толстой', '1000')
            my_book.get_data()
            my_book.get_name()

        elif task_number == 3:
            my_stadium = Stadium('Спартак', '2000', 'Россия', 'Москва', '10000')
            my_stadium.get_data()
            my_stadium.get_name()
            my_stadium.get_country()
            my_stadium.set_city()
            my_stadium.get_data()
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
