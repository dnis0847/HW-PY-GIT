from typing import List
from .pizza import Pizza
from .topping import Topping

class Order:
    def __init__(self):
        self.pizzas: List[Pizza] = []
        self.total_sales: float = 0
        self.total_pizzas: int = 0

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def calculate_total(self) -> float:
        total = sum(pizza.calculate_price() for pizza in self.pizzas)
        return total

    def finalize_order(self, payment_method: str):
        total = self.calculate_total()
        self.total_sales += total
        self.total_pizzas += len(self.pizzas)
        self.save_order_to_file()
        self.pizzas.clear()
        return total

    def save_order_to_file(self):
        with open('orders.txt', 'a') as file:
            for pizza in self.pizzas:
                file.write(f'{pizza.name}: {pizza.get_description()}, Price: {pizza.calculate_price()}\n')
            file.write(f'Total: {self.calculate_total()}\n\n')

    def get_statistics(self):
        return {
            'total_pizzas': self.total_pizzas,
            'total_sales': self.total_sales,
            'profit': self.total_sales * 0.3  # Предположим, что прибыль составляет 30%
        }