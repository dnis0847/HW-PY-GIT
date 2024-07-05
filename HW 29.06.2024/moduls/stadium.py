'''
Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город,
вместимость. Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
'''

class Stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def post_data(self):
        print(f"Название: {self.name}, дата открытия: {self.date}, страна: {self.country}, город: {self.city}, "
              f"вместимость: {self.capacity}")

    def get_data(self):
        print(f"Название: {self.name}, дата открытия: {self.date}, страна: {self.country}, город: {self.city}, "
              f"вместимость: {self.capacity}")

    def get_name(self):
        return print(f"Название: {self.name}")

    def get_date(self):
        return print(f"Дата открытия: {self.date}")

    def get_country(self):
        return print(f"Страна: {self.country}")

    def get_city(self):
        return print(f"Город: {self.city}")

    def get_capacity(self):
        return print(f"Вместимость: {self.capacity}")

    def set_name(self):
        self.name = input("Введите новое название: ")

    def set_date(self):
        self.date = input("Введите новую дату: ")

    def set_country(self):
        self.country = input("Введите новую страну: ")

    def set_city(self):
        self.city = input("Введите новый город: ")

    def set_capacity(self):
        self.capacity = input("Введите новую вместимость: ")