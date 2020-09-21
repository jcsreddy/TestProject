class A:
    def __init__(self):
        print("I am in class A")

class B(A):
    def __init__(self):
        A.__init__(self)
        print("I am in class B")

# b=A()
b=B()
