
class Animal:
    def __init__(self):
        self.sound = "Generic Animal Sound"
        self.favorite_food = "Generic Food"
        self.habitat = "Generic Habitat"

    def speak(self):
        return self.sound

    def eat(self):
        print(f"I am eating {self.favorite_food}")

    def live(self):
        print(f"I live in {self.habitat}")

class Dog(Animal):
    def __init__(self, sound, favorite_food):
        super().__init__()
        self.sound = sound
        self.favorite_food = favorite_food


if __name__ == '__main__':
    animal = Animal()
    dog = Dog(sound='Woof!', favorite_food='Dog food')

    print('Animal Speaking')
    print(animal.speak())
    print('-'*80)

    print('Dog Behavior')
    dog.eat()
    print(dog.speak())
    print('-'*80)
