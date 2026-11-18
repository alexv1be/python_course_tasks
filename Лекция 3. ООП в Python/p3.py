"""Практика № 3. Товары, корзина и история заказов магазина."""

class Product:
    """Хранит название, цену за штуку, остаток и категорию товара."""

    def __init__(self, name: str, price: float, stock: int, category: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category


class ShoppingCart:
    """Хранит выбранные количества и резервирует товары на складе."""

    def __init__(self):
        self.items = {}  # Ключ — объект Product, значение — количество.

    def add_product(self, product: Product, quantity: int = 1):
        """Добавить положительное количество товара при наличии на складе."""
        if quantity <= 0:
            raise ValueError("Добавляемое количество должно быть положительным.")
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            product.stock -= quantity
        else:
            print(f"Недостаточно товара '{product.name}' на складе.")

    def remove_product(self, product: Product):
        """Убрать товар из корзины и вернуть его количество на склад."""
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]

    def update_quantity(self, product: Product, new_quantity: int):
        """Изменить количество зарезервированного товара или убрать его при нуле."""
        if new_quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным.")
        if new_quantity == 0:
            self.remove_product(product)
            return
        if product in self.items:
            diff = new_quantity - self.items[product]
            if product.stock >= diff:
                self.items[product] = new_quantity
                product.stock -= diff
            else:
                print("Недостаточно товара на складе для обновления.")


class Order:
    """Хранит состав заказа и его итоговую стоимость."""

    def __init__(self, cart_items: dict, discount: float = 0.0, tax: float = 0.1):
        self.items = cart_items.copy()
        self.discount = discount
        self.tax = tax
        self.total_price = self.calculate_total()

    def calculate_total(self):
        """Применить скидку, начислить налог на остаток и округлить сумму."""
        base_price = sum(product.price * quantity for product, quantity in self.items.items())
        discounted_price = base_price * (1 - self.discount)
        final_price = discounted_price * (1 + self.tax)
        return round(final_price, 2)


class Customer:
    """Хранит имя, электронную почту и историю заказов покупателя."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.order_history = []

    def checkout(self, cart: ShoppingCart, discount: float = 0.0):
        """Оформить заказ из корзины и записать его в историю покупателя."""
        if not cart.items:
            return "Корзина пуста!"

        order = Order(cart.items, discount)
        self.order_history.append(order)
        cart.items.clear()
        return f"Заказ успешно оформлен. Итоговая сумма: {order.total_price}"
