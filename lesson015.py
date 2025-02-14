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

