class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} pracuje na stanowisku {self.position}"


class Teacher(Employee):

    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} i uczy {self.subject}"


class Doctor(Employee):

    def __init__(self, name, position, specialization):
        super().__init__(name, position)
        self.specialization = specialization

    def __str__(self):
        return f"{super().__str__()} i specjalizuje się w {self.specialization}"


class Engineer(Employee):

    def __init__(self, name, position, building_spec):
        super().__init__(name, position)
        self.building_spec = building_spec

    def __str__(self):
        return f"{super().__str__()} i projektuje {self.building_spec}"


employees = [
    Employee('Jan', 'Budowlaniec'),
    Teacher('Anna', "Nauczycielka", "Język Polski"),
    Doctor('Ryszard', "Lekarz", 'Ortopedia'),
    Engineer('Tomasz', 'Architekt', "Mosty")
]

for employee in employees:
    print(employee)
