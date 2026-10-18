# Практика #4: Симулятор космического корабля

import random


class SpaceShip:
    # Атрибуты для управления топливом, состоянием корпуса и скоростью
    def __init__(self, name: str, fuel: float, hull: float):
        self.name = name
        self.fuel = fuel
        self.hull = hull
        self.speed = 0.0

    def change_speed(self, amount: float):
        fuel_cost = abs(amount) * 0.5
        if self.fuel >= fuel_cost:
            self.speed += amount
            self.fuel -= fuel_cost
            print(f"Скорость изменена. Текущая скорость: {self.speed}, остаток топлива: {self.fuel}")
        else:
            print("Недостаточно топлива для маневра!")

    def take_damage(self, damage: float):
        self.hull -= damage
        if self.hull <= 0:
            print(f"Корабль {self.name} уничтожен!")
        else:
            print(f"Прочность корпуса снижена до {self.hull}%")


class CrewMember:
    # Контролирует здоровье, навыки и роли в команде
    def __init__(self, name: str, role: str, skill_level: int):
        self.name = name
        self.role = role
        self.health = 100.0
        self.skill_level = skill_level

    def perform_action(self, ship: SpaceShip):
        if self.health <= 0:
            print(f"{self.name} не может действовать.")
            return

        if self.role.lower() == "инженер":
            repair_amount = self.skill_level * 2
            ship.hull = min(100.0, ship.hull + repair_amount)
            print(f"Инженер {self.name} чинит корабль. Корпус восстановлен до {ship.hull}%")
        elif self.role.lower() == "пилот":
            print(f"Пилот {self.name} выполняет уклонение. Риск столкновения снижен.")


class Mission:
    # Определяет цели, ресурсы и возможные события (аварии, астероиды)
    def __init__(self, target: str, ship: SpaceShip, crew: list):
        self.target = target
        self.ship = ship
        self.crew = crew

    def trigger_random_event(self):
        events = ["авария", "встреча с астероидом", "спокойный полет"]
        current_event = random.choice(events)

        print(f"\n--- Событие миссии: {current_event.upper()} ---")

        if current_event == "встреча с астероидом":
            damage = random.randint(15, 40)
            print(f"Астероид нанес {damage} урона!")
            self.ship.take_damage(damage)
        elif current_event == "авария":
            fuel_loss = random.randint(10, 25)
            print(f"Утечка топлива в размере {fuel_loss} ед.")
            self.ship.fuel -= fuel_loss
        else:
            print("Полет проходит в штатном режиме.")

        # Даем возможность экипажу отреагировать
        for member in self.crew:
            member.perform_action(self.ship)