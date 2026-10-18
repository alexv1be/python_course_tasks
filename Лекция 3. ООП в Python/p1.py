# Практика #1

class Employee:
    def __init__(self, id: int, name: str, base_money: float):
        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salaries(self):
        return self.base_money

class Manager(Employee):
    def __init__(self, id: int, name: str, base_money: float, bonus: float):
        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salaries(self):
        return super().calculate_salaries() + self.bonus

class Developer(Employee):
    def __init__(self, id: int, name: str, base_money: float, projects: int):
        super().__init__(id, name, base_money)
        self.projects = projects

    def calculate_salaries(self):
        return super().calculate_salaries() + self.projects * 10_000


ivan = Employee(1, "иван", 20000)
alex = Manager(2, "алекс", 20000, 5000)
grigo = Developer(3, "григо", 20000, 5)

print(ivan.name, ivan.calculate_salaries())
print(alex.name, alex.calculate_salaries())
print(grigo.name, grigo.calculate_salaries())