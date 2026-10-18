# Практика #2

class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"транспорт - {self.name}"

class Car(Transport):
    def description(self):
        return f"этот транспорт - {self.name}, это машина. у нее есть колеса и она ездит по дорогам"

class Plane(Transport):
    def description(self):
        return f"этот транспорт - {self.name}, это самолет. у него есть крылья и он летает в небе"

class Bike(Transport):
    def description(self):
        return f"этот транспорт - {self.name}, это мотоцикл. у него есть колеса и он небольшой, а также быстрый"

# Демонстрация вызова метода
camry = Car("Camry")
plane = Plane("Boeing")
bike = Bike("ИЖ")

print(camry.description())
print(plane.description())
print(bike.description())