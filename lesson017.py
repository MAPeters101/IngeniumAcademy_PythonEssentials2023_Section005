

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def helper1(parameter):
        pass

    @staticmethod
    def calculate_area_static(radius):
        #self.area()
        return 3.14 * radius * radius

    def area(self):
        return self.calculate_area_static(radius=self.radius)
        # return 3.14 * self.radius * self.radius


if __name__ == '__main__':
    circle = Circle(radius=10)

    print("Calculating Area without static method")
    print(circle.area())
    print('-'*30)

    print("Calculating Area using static method")
    print(circle.calculate_area_static(radius=10))
    print('-'*30)


