class Car:
    color = "white"


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof"


if __name__ == '__main__':
    my_car = Car()
    print(my_car.color)

    my_second_car = Car()
    print(my_second_car.color)
    print()

    dog1 = Dog(name="Rocky")
    dog2 = Dog(name="Sandy")
    print(dog1.name, dog2.name)

    print(dog1.bark(), dog2.bark())

