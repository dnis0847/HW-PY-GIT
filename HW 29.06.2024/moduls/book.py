'''
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def post_data(self):
        self.name = input("Введите название: ")
        self.year = input("Введите год: ")
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = input("Введите цену: ")

    def get_data(self):
        print(f"Название: {self.name}, год: {self.year}, издатель: {self.publisher}, "
              f"жанр: {self.genre}, автор: {self.author}, цена: {self.price}")

    def get_name(self):
        return print(f"Название: {self.name}")

    def get_year(self):
        return print(f"Год: {self.year}")

    def get_publisher(self):
        return print(f"Издатель: {self.publisher}")

    def get_genre(self):
        return print(f"Жанр: {self.genre}")

    def get_author(self):
        return print(f"Автор: {self.author}")

    def get_price(self):
        return print(f"Цена: {self.price}")

    def set_name(self):
        self.name = input("Введите новое название: ")

    def set_year(self):
        self.year = input("Введите новый год: ")

    def set_publisher(self):
        self.publisher = input("Введите нового издателя: ")

    def set_genre(self):
        self.genre = input("Введите новый жанр: ")

    def set_author(self):
        self.author = input("Введите нового автора: ")

    def set_price(self):
        self.price = input("Введите новую цену: ")