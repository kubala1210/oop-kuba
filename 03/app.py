class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def describe(self):
        return f"{self.name} pracuje na stanowisku {self.position}"


class Teacher(Employee):

    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject

    def describe(self):
        return f"{super().describe()} i uczy {self.subject}"


class Doctor(Employee):

    def __init__(self, name, position, specialization):
        super().__init__(name, position)
        self.specialization = specialization

    def describe(self):
        return f"{super().describe()} i specjalizuje się w {self.specialization}"


class Engineer(Employee):

    def __init__(self, name, position, building_spec):
        super().__init__(name, position)
        self.building_spec = building_spec

    def describe(self):
        return f"{super().describe()} i projektuje {self.building_spec}"


employees = [
    Employee('Jan', 'Budowlaniec'),
    Teacher('Anna', "Nauczycielka", "Język Polski"),
    Doctor('Ryszard', "Lekarz", 'Ortopedia'),
    Engineer('Tomasz', 'Architekt', "Mosty")
]

for employee in employees:
    print(employee.describe())
