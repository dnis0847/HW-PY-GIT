from .pizza import Pizza, Margherita, Pepperoni, Hawaiian, Funghi, Vegetarian, CustomPizza

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == 'Margherita':
            return Margherita()
        elif pizza_type == 'Pepperoni':
            return Pepperoni()
        elif pizza_type == 'Hawaiian':
            return Hawaiian()
        elif pizza_type == 'Funghi':
            return Funghi()
        elif pizza_type == 'Vegetarian':
            return Vegetarian()
        else:
            return CustomPizza()