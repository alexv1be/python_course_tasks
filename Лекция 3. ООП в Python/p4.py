"""Практика № 4. Корабль, экипаж и случайные события миссии."""

import random


class SpaceShip:
    """Хранит запас топлива, прочность корпуса в процентах и скорость."""

    def __init__(self, name: str, fuel: float, hull: float):
        self.name = name
        self.fuel = fuel
        self.hull = hull
        self.speed = 0.0

    def change_speed(self, amount: float):
        """Изменить скорость, потратив 0.5 единицы топлива на единицу изменения."""
        fuel_cost = abs(amount) * 0.5
        if self.fuel >= fuel_cost:
            self.speed += amount
            self.fuel -= fuel_cost
            print(f"Скорость изменена. Текущая скорость: {self.speed}, остаток топлива: {self.fuel}")
        else:
            print("Недостаточно топлива для маневра!")

    def take_damage(self, damage: float):
        """Уменьшить прочность корпуса вплоть до нуля."""
        self.hull = max(0.0, self.hull - damage)
        if self.hull <= 0:
            print(f"Корабль {self.name} уничтожен!")
        else:
            print(f"Прочность корпуса снижена до {self.hull}%")


class CrewMember:
    """Член экипажа с ролью, здоровьем и уровнем навыка."""

    def __init__(self, name: str, role: str, skill_level: int):
        self.name = name
        self.role = role
        self.health = 100.0
        self.skill_level = skill_level

    def perform_action(self, ship: SpaceShip):
        """Выполнить действие по роли, если член экипажа может действовать."""
        if self.health <= 0:
            print(f"{self.name} не может действовать.")
            return

        if self.role.lower() == "инженер":
            if ship.hull <= 0:
                return
            repair_amount = self.skill_level * 2
            ship.hull = min(100.0, ship.hull + repair_amount)
            print(f"Инженер {self.name} чинит корабль. Корпус восстановлен до {ship.hull}%")
        elif self.role.lower() == "пилот":
            print(f"Пилот {self.name} выполняет уклонение. Риск столкновения снижен.")


class Mission:
    """Связывает цель полёта с кораблём и экипажем."""

    def __init__(self, target: str, ship: SpaceShip, crew: list):
        self.target = target
        self.ship = ship
        self.crew = crew

    def trigger_random_event(self):
        """Обработать случайное событие и дать экипажу отреагировать."""
        events = ["авария", "встреча с астероидом", "спокойный полет"]
        current_event = random.choice(events)

        print(f"\n--- Событие миссии: {current_event.upper()} ---")

        if current_event == "встреча с астероидом":
            damage = random.randint(15, 40)
            print(f"Астероид нанес {damage} урона!")
            self.ship.take_damage(damage)
        elif current_event == "авария":
            fuel_loss = min(self.ship.fuel, random.randint(10, 25))
            print(f"Утечка топлива в размере {fuel_loss} ед.")
            self.ship.fuel -= fuel_loss
        else:
            print("Полет проходит в штатном режиме.")

        for member in self.crew:
            member.perform_action(self.ship)
