class Animal:

    def __init__(self, name='Zwierze'):
        self.name = name

    def __str__(self):
        return f"{self.name} wydaje dźwięk"


class Dog(Animal):

    def __str__(self):
        return f"Pies {self.name} szczeka: Hau! Hau!"


class Cat(Animal):

    def __str__(self):
        return f"Kot {self.name} miauczy: Miau! Miau!"


class Cow(Animal):

    def __str__(self):
        return f"Krowa {self.name} muczy: Muu! Muu!"


animals = [
    Animal(),
    Dog('Burek'),
    Cat('Mruczek'),
    Cow('Halinka')
]

for animal in animals:
    print(animal)
