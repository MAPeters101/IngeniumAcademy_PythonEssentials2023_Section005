class A:
    def show(self):
        print("Method from class A")

class C(A):
    # def show(self):
    #     print("Method from class C")
    pass

class E(A):
    # def show(self):
    #     print("Method from class B")
    pass

class D(E, C): pass


if __name__ == '__main__':
    #print(D.__mro__)

    d = D()
    d.show()

    print(D.mro())


