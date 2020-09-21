class classA:
    def helloword(self):
        print("Hello from Class A")

class classB:
    def helloword(self):
        print("Hello from Class B")

class classC(classB, classA):
    def methodC(self):
        print("Method from Class C")

c=classC()
c.helloword()
print(classC.mro())


