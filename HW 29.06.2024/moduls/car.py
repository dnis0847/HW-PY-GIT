'''
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя,
объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ
к отдельным полям через методы класса.
'''


class Car:
    def __init__(self, name, year, brand, engine_capacity, color, price):
        self.name = name
        self.year = year
        self.brand = brand
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    # Метод для ввода данных
    def post_data(self):
        self.name = input("Введите название: ")
        self.year = input("Введите год: ")
        self.brand = input("Введите производителя: ")
        self.engine_capacity = input("Введите объем двигателя: ")
        self.color = input("Введите цвет: ")
        self.price = input("Введите цену: ")

    # Метод для вывода данных
    def get_data(self):
        print(f"Название: {self.name}, год: {self.year}, производитель: {self.brand}, "
              f"объем двигателя: {self.engine_capacity}, цвет: {self.color}, цена: {self.price}")

    # Методы для доступа к отдельным полям
    def get_name(self):
        return print(f"Название: {self.name}")

    def get_year(self):
        return print(f"Год: {self.year}")

    def get_brand(self):
        return print(f"Производитель: {self.brand}")

    def get_engine_capacity(self):
        return print(f"Объем двигателя: {self.engine_capacity}")

    def get_color(self):
        return print(f"Цвет: {self.color}")

    def get_price(self):
        return print(f"Цена: {self.price}")

    # Методы для изменения данных
    def set_name(self):
        self.name = input("Введите новое название: ")

    def set_year(self):
        self.year = input("Введите новый год: ")

    def set_brand(self):
        self.brand = input("Введите нового производителя: ")

    def set_engine_capacity(self):
        self.engine_capacity = input("Введите новый объем двигателя: ")

    def set_color(self):
        self.color = input("Введите новый цвет: ")

    def set_price(self):
        self.price = input("Введите новую цену: ")
