class classA:
    def methodA(self):
        print("I am in Class A")

    def helloworld(self):           #overridden in class B
        print("Hello from class A")

class classB(classA):
    def methodB(self):
        print("I am in Class B")

    def helloworld(self):           #over rides method in Class A
        print("Hello from class B")

class classC(classB):
    def methodC(self):
        print("I am in Class C")

c=classC()
c.methodC()
c.methodB()
c.methodA()
c.helloworld()