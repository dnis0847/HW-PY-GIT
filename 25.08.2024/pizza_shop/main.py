from models.pizza import Pizza
from models.pizza_factory import PizzaFactory
from models.order import Order
from models.topping import Topping

if __name__ == '__main__':
    factory = PizzaFactory()
    order = Order()

    # Пользователь выбирает пиццу
    margherita = factory.create_pizza('Margherita')
    pepperoni = factory.create_pizza('Pepperoni')

    # Пользователь добавляет топпинги
    margherita.add_topping(Topping('Olives', 1.5))
    pepperoni.add_topping(Topping('Jalapeno', 1.0))

    # Добавляем пиццу в заказ
    order.add_pizza(margherita)
    order.add_pizza(pepperoni)

    # Финализируем заказ
    total = order.finalize_order('card')
    print(f'Total amount to pay: ${total}')

    # Печать статистики
    stats = order.get_statistics()
    print(f'Total pizzas sold: {stats["total_pizzas"]}')
    print(f'Total sales: ${stats["total_sales"]}')
    print(f'Profit: ${stats["profit"]}')
