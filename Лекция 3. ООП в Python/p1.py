"""Практика № 1. Наследование и расчёт зарплаты сотрудников."""

class Employee:
    """Сотрудник с идентификатором, именем и окладом."""

    def __init__(self, id: int, name: str, base_money: float):
        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salaries(self):
        """Вернуть базовый оклад сотрудника."""
        return self.base_money

class Manager(Employee):
    """Менеджер с фиксированной премией."""

    def __init__(self, id: int, name: str, base_money: float, bonus: float):
        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salaries(self):
        """Вернуть оклад с учётом премии."""
        return super().calculate_salaries() + self.bonus

class Developer(Employee):
    """Разработчик с доплатой за выполненные проекты."""

    def __init__(self, id: int, name: str, base_money: float, projects: int):
        super().__init__(id, name, base_money)
        self.projects = projects

    def calculate_salaries(self):
        """Вернуть оклад и доплату в 10 000 за каждый проект."""
        return super().calculate_salaries() + self.projects * 10_000


if __name__ == "__main__":
    ivan = Employee(1, "иван", 20000)
    alex = Manager(2, "алекс", 20000, 5000)
    grigo = Developer(3, "григо", 20000, 5)

    for employee in (ivan, alex, grigo):
        print(employee.name, employee.calculate_salaries())
