

class Cat:
    type = 'cat'

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} says: Meow')


class Dog:
    type = 'dog'

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} says: Woff!')


class Rabbit:
    type = 'rabbit'

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} says: Squeak, Squeak')


class Snake:
    type = 'snake'

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} says: Sssss-S-s-s')


class Pony:
    type = 'Pony'

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} says: Neigh!')


PETS = [
    Dog('Luna'),
    Cat('Lily'),
    Dog('Charlie'),
    Cat('Cleo'),
    Rabbit('Oliver'),
    Dog('Bella'),
    Dog('Baxter'),
    Snake('Gusty'),
    Cat('Milo'),
    Pony('Applejack'),
]


class Person:

    def __init__(self, name):
        self.name = name
        self.pets = []

    def speak(self):
        print(f'Hi, my name is {self.name}. I like pets')

    def add_pet(self, pet):
        self.pets.append(pet)

    def show_available_pets(self):
        for pet in self.pets:
            print(pet)


if __name__ == '__main__':
    alice = Person(name='Alice')
    alice.speak()

    print(PETS)
    dog = PETS.pop(0)
    alice.add_pet(dog)
    alice.show_available_pets()

