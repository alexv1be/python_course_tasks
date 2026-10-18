# Практика #3: Онлайн-магазин

class Product:
    # Включает информацию о цене, наличии на складе и категории товара
    def __init__(self, name: str, price: float, stock: int, category: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Словарь вида {Объект_Product: количество}

    # Позволяет добавлять, удалять и обновлять количество товаров
    def add_product(self, product: Product, quantity: int = 1):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            product.stock -= quantity
        else:
            print(f"Недостаточно товара '{product.name}' на складе.")

    def remove_product(self, product: Product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]

    def update_quantity(self, product: Product, new_quantity: int):
        if product in self.items:
            diff = new_quantity - self.items[product]
            if product.stock >= diff:
                self.items[product] = new_quantity
                product.stock -= diff
            else:
                print("Недостаточно товара на складе для обновления.")


class Order:
    # Обрабатывает процесс покупки, включая расчет цены с учетом скидок и налогов
    def __init__(self, cart_items: dict, discount: float = 0.0, tax: float = 0.1):
        self.items = cart_items.copy()
        self.discount = discount
        self.tax = tax
        self.total_price = self.calculate_total()

    def calculate_total(self):
        base_price = sum(product.price * quantity for product, quantity in self.items.items())
        discounted_price = base_price * (1 - self.discount)
        final_price = discounted_price * (1 + self.tax)
        return round(final_price, 2)


class Customer:
    # Управляет информацией о пользователе и его истории заказов
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.order_history = []

    def checkout(self, cart: ShoppingCart, discount: float = 0.0):
        if not cart.items:
            return "Корзина пуста!"

        order = Order(cart.items, discount)
        self.order_history.append(order)
        cart.items.clear()
        return f"Заказ успешно оформлен. Итоговая сумма: {order.total_price}"