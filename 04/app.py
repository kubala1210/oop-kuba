class Animal:

    def __init__(self, name='Zwierze'):
        self.name = name

    def make_sound(self):
        return f"{self.name} wydaje dźwięk"


class Dog(Animal):

    def make_sound(self):
        return f"Pies {self.name} szczeka: Hau! Hau!"


class Cat(Animal):

    def make_sound(self):
        return f"Kot {self.name} miauczy: Miau! Miau!"


class Cow(Animal):

    def make_sound(self):
        return f"Krowa {self.name} muczy: Muu! Muu!"


animals = [
    Animal(),
    Dog('Burek'),
    Cat('Mruczek'),
    Cow('Halinka')
]

for animal in animals:
    print(animal.make_sound())
