class classA:
    def methodA(self):
        print("I am in Class A")
    def helloworld(self):
        print("Hello world from Class A")

class classB:
    def methodB(self):
        print("I am in Class B")
    def helloworld(self):
        print("Hello world from Class B")

class classC(classB, classA):
    def methodC(self):
        print("I am in Class C")
    # def helloworld(self):
    #     print("Hello world from Class C")

c = classC()
c.methodC()
c.methodB()
c.methodA()
c.helloworld()
