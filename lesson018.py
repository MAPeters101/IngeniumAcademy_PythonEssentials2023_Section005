class A: pass

class C(A): pass

class B(A): pass

class D(B, C): pass


if __name__ == '__main__':
    print(D.__mro__)


