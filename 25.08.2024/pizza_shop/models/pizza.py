from abc import ABC, abstractmethod
from typing import List
from .topping import Topping


class Pizza(ABC):
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.toppings: List[Topping] = []

    def add_topping(self, topping: Topping):
        self.toppings.append(topping)

    def calculate_price(self) -> float:
        total_price = self.base_price + sum(topping.price for topping in self.toppings)
        return total_price

    @abstractmethod
    def get_description(self) -> str:
        pass


class Margherita(Pizza):
    def __init__(self):
        super().__init__('Margherita', 8.0)

    def get_description(self) -> str:
        return "Tomato sauce, mozzarella"


class Pepperoni(Pizza):
    def __init__(self):
        super().__init__('Pepperoni', 10.0)

    def get_description(self) -> str:
        return "Tomato sauce, mozzarella, pepperoni"


class Hawaiian(Pizza):
    def __init__(self):
        super().__init__('Hawaiian', 12.0)

    def get_description(self) -> str:
        return "Tomato sauce, mozzarella, ham, pineapple"


class Funghi(Pizza):
    def __init__(self):
        super().__init__('Funghi', 12.0)

    def get_description(self) -> str:
        return "Tomato sauce, mozzarella, mushrooms"


class Vegetarian(Pizza):
    def __init__(self):
        super().__init__('Vegetarian', 10.0)

    def get_description(self) -> str:
        return "Tomato sauce, mozzarella, vegetables"


class CustomPizza(Pizza):
    def __init__(self):
        super().__init__('Custom Pizza', 7.0)

    def get_description(self) -> str:
        return "Custom ingredients"
