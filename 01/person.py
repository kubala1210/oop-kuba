class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"Cześć, mam na imię {self.name}, mam {self.age} lat, i mieszkam w mieście {self.city}"


# person_1 = Person('Jan', 25, 'Warszawa')
# person_2 = Person('Anna', 30, 'Kraków')
# person_3 = Person('Piotr', 35, 'Gdańsk')

people = [
    Person('Jan', 25, 'Warszawa'),
    Person('Anna', 30, 'Kraków'),
    Person('Piotr', 35, 'Gdańsk'),
]

for person in people:
    print(person.introduce())
