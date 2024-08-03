'''
Создайте класс "Самолет". Наполните его необходимыми характеристиками и методами. Реализуйте упаковку и распаковку
объектов класса "Самолет" с использованием модуля json.
'''

import json
import sys
import os


class Plane:
    def __init__(self, _brand, _model, _year, _max_weight):
        self.brand = _brand
        self.model = _model
        self.year = _year
        self.max_weight = _max_weight

    def __str__(self):
        """
        Возвращает строковое представление объекта класса "Самолет".
        """
        return (f"Бренд: {self.brand}, модель: {self.model}, год выпуска: {self.year}, "
                f"максимальная вместимость: {self.max_weight}")

    @property
    def brand(self):
        """
        Возвращает бренд объекта класса "Самолет".
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """
        Устанавливает бренд объекта класса "Самолет".
        """
        self._brand = brand

    @property
    def model(self):
        """
        Возвращает модель объекта класса "Самолет".
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Устанавливает модель объекта класса "Самолет".
        """
        self._model = model

    @property
    def year(self):
        """
        Возвращает год выпуска объекта класса "Самолет".
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Устанавливает год выпуска объекта класса "Самолет".
        """
        self._year = year

    @property
    def max_weight(self):
        """
        Возвращает максимальную вместимость объекта класса "Самолет".
        """
        return self._max_weight

    @max_weight.setter
    def max_weight(self, max_weight):
        """
        Устанавливает максимальную вместимость объекта класса "Самолет".
        """
        self._max_weight = max_weight

    def save_to_file(self, filename):
        """
        Сохраняет объект класса "Самолет" в файл.
        """
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load_from_file(cls, filename):
        """
        Загружает объект класса "Самолет" из файла.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(**data)


def main():
    plane = Plane('Boeing', '737', 2020, 10000)
    plane.save_to_file('plane.json')
    new_plane = Plane.load_from_file('plane.json')
    print(new_plane)
    other_plane = Plane('Airbus', 'A320', 2021, 12000)
    other_plane.save_to_file('other_plane.json')
    new_other_plane = Plane.load_from_file('other_plane.json')
    print(new_other_plane)


if __name__ == '__main__':
    main()
