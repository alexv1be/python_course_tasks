"""Практика № 2. Полиморфизм описаний транспорта."""

class Transport:
    """Базовый транспорт с названием."""

    def __init__(self, name):
        self.name = name

    def description(self):
        """Вернуть общее описание транспорта."""
        return f"транспорт - {self.name}"

class Car(Transport):
    """Автомобиль, который ездит по дорогам."""

    def description(self):
        """Вернуть описание автомобиля."""
        return f"этот транспорт - {self.name}, это машина. у нее есть колеса и она ездит по дорогам"

class Plane(Transport):
    """Самолёт, который летает на крыльях."""

    def description(self):
        """Вернуть описание самолёта."""
        return f"этот транспорт - {self.name}, это самолет. у него есть крылья и он летает в небе"

class Bike(Transport):
    """Мотоцикл."""

    def description(self):
        """Вернуть описание мотоцикла."""
        return f"этот транспорт - {self.name}, это мотоцикл. у него есть колеса и он небольшой, а также быстрый"

if __name__ == "__main__":
    vehicles = (Transport("обычный транспорт"), Car("Camry"), Plane("Boeing"), Bike("ИЖ"))
    for vehicle in vehicles:
        print(vehicle.description())
